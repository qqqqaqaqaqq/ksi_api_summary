import traceback

import app.services.api_setup as ksi_function
from app.models.order import ResponseBody as OrderResponseBody
from app.models.commonResponse import ResponseBody as ComResponseBody

# ==================
# ==== 거래 주문 ====
# ==================

def order(
    order_type: str,   # 주문 타입 매수 코드 : TTTT1002U, 매도 코드 : TTTT1006U
    ksi_api: str,      # KSI API 인스턴스
    ticker: str,       # 종목 코드
    EXCD: str,       # 종목 메타 정보 (거래소 등)
    askbid: dict,      # 호가 정보 {ask1, bid1, aks2, bid2}
    last: float        # 직전 체결가
):
    # 최우선 매도/매수 호가
    ask1 = askbid.get("ask1")
    bid1 = askbid.get("bid1")

    # 호가 또는 가격 정보가 없으면 주문 불가
    if ask1 is None or bid1 is None or not last or last <= 0:
        return ComResponseBody(
            status=1002,
            http_status=None,
            message="[order] NO_QUOTE",
            data=None
        )
    
    uuid = None
    try:
        # 매수
        if order_type == "TTTT1002U":
            # 매도 1호가가 마지막 체결가 대비 1% 이상 벌어지면 주문 취소
            if float((ask1 - last) / last) > 0.01:     
                return ComResponseBody(
                    status=1001,
                    http_status=None,
                    message="호가창 변동 문제로 매수가 취소 됩니다",
                    data=None
                )
                
            order_buy:OrderResponseBody = ksi_function.ksi_order(ksi_api=ksi_api, order_type=order_type, OVRS_EXCG_CD=EXCD, PDNO=ticker, ORD_QTY=1, OVRS_ORD_UNPR=ask1)
            trade_data:dict = order_buy.output
            uuid = trade_data.get("ODNO")
        
        # 매도
        elif order_type == "TTTT1006U":
            # 매수 1호가가 마지막 체결가 대비 1% 이상 벌어지면 주문 취소
            if float((last - bid1) / last) > 0.01:
                print("호가창 변동 문제로 매도가 취소 됩니다.")
                return ComResponseBody(
                    status=1001,
                    http_status=None,
                    message="호가창 변동 문제로 매도가 취소 됩니다",
                    data=None
                )
            
            order_sell:OrderResponseBody = ksi_function.ksi_order(ksi_api=ksi_api, order_type=order_type, OVRS_EXCG_CD=EXCD, PDNO=ticker, ORD_QTY=1, OVRS_ORD_UNPR=bid1)
            trade_data:dict = order_sell.output
            uuid = trade_data.get("ODNO")
        else:
            return ComResponseBody(
                status=1003,
                http_status=None,
                message="INVALID_ORDER_TYPE",
                data=None
            ) 

        return ComResponseBody(
            status=0,
            http_status=None,
            message="ORDER_PLACED",
            data=uuid
        ) 
    
    except Exception as e:
        print(e)
        traceback.print_exc()
        return ComResponseBody(
            status=9001,
            http_status=None,
            message=f"[order] : {str(e)}",
            data=None
        )         

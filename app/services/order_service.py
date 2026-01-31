import traceback

import app.services.api_setup as ksi_function
from app.models.order import ResponseBody as OrderResponseBody

# ==================
# ==== 거래 주문 ====
# ==================
def order(order_type:str, ksi_api:str, ticker:str, value:dict, askbid:dict, last:float):
    try:
        if order_type == "TTTT1002U":
            if askbid.get("ask1") - last > 1.00:
                print("호가창 변동 문제로 매수가 취소 됩니다.")
                

            order_buy:OrderResponseBody = ksi_function.ksi_order(ksi_api=ksi_api, order_type=order_type, OVRS_EXCG_CD=value.get("ovrs_excg_cd"), PDNO=ticker, ORD_QTY=1, OVRS_ORD_UNPR=askbid.get("bid1"))
            trade_data:dict = order_buy.output
            uuid = trade_data.get("ODNO")

        elif order_type == "TTTT1006U":
            if last - askbid.get("bid1") > 1.00:
                print("호가창 변동 문제로 매도가 취소 됩니다.")
                
            order_sell:OrderResponseBody = ksi_function.ksi_order(ksi_api=ksi_api, order_type=order_type, OVRS_EXCG_CD=value.get("ovrs_excg_cd"), PDNO=ticker, ORD_QTY=1, OVRS_ORD_UNPR=askbid.get("ask1"))
            trade_data:dict = order_sell.output
            uuid = trade_data.get("ODNO")

        return uuid
    except Exception as e:
        print(e)
        traceback.print_exc()

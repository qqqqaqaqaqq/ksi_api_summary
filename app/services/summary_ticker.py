import traceback

from app.services.utils import to_float
from app.models.commonResponse import ResponseBody as ComResponseBody

# ==================
# ==== 계좌 요약 ====
# ==================
def summary_ticker(data:dict):
    """
    계좌 데이터 1건을 요약 dict로 변환
    - 현금: 사용 가능 금액
    - 종목: 연계 거래소 코드 / 실제 해외 거래소 / 평균단가 / 수량 / 수익률 / 현재가
    """    
    summary:dict = {}
    try:
        if not data:
            return ComResponseBody(
                status=1002,
                http_status=None,
                message=f"[summary_ticker] None Data",
                data=None
            )
        
        currency = data.get("crcy_cd")

        is_cash = currency in ("USD", "KRW")

        if is_cash:
            summary[currency] = {
                "available_cash": to_float(data.get("frcr_drwg_psbl_amt_1"))
            }
        else:
            ticker = data.get("pdno")
            summary[ticker] = {
                "item_lnkg_excg_cd": data.get("item_lnkg_excg_cd"),
                "ovrs_excg_cd": data.get("ovrs_excg_cd"),
                "avg_price": to_float(data.get("frcr_pchs_amt")),
                "quantity": to_float(data.get("ccld_qty_smtl1")),
                "current_profit_rate": to_float(data.get("evlu_pfls_rt1")),
                "ovrs_now_pric1" : to_float(data.get("ovrs_now_pric1"))
            }
        
        return ComResponseBody(
            status=0,
            http_status=None,
            message="SUMMARY_OK",
            data=summary
        )
          
    except Exception as e:
        print(e)
        traceback.print_exc()
        return ComResponseBody(
            status=9001,
            http_status=None,
            message= f"[summary_ticker] {str(e)}",
            data=None
        )

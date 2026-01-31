import traceback

from app.services.utils import to_float


# ==================
# ==== 계좌 요약 ====
# ==================
def summary_ticker(data:dict):
    summary:dict = {}
    try:
        ticker = data.get("crcy_cd")

        if ticker != "USD" and ticker != "KRW":
            ticker = data.get("pdno")
            summary[ticker] = {
                "item_lnkg_excg_cd": data.get("item_lnkg_excg_cd"),
                "ovrs_excg_cd": data.get("ovrs_excg_cd"),
                "avg_price": to_float(data.get("frcr_pchs_amt")),
                "quantity": to_float(data.get("ccld_qty_smtl1")),
                "current_profit_rate": to_float(data.get("evlu_pfls_rt1")),
                "ovrs_now_pric1" : to_float(data.get("ovrs_now_pric1"))
            }
        else:
            summary[ticker] = {
                "avaliable_cash": to_float(data.get("frcr_drwg_psbl_amt_1"))
            }
    except Exception as e:
        print(e)
        traceback.print_exc()

    return summary
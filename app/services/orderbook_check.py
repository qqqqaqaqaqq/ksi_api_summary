import traceback
from app.models.orderbook import ResponseBody as OrderBookResponseBody
from app.services.utils import to_float
import app.services.api_setup as ksi_function

# ==================
# ==== 오더 북  =====
# ==================
def orderbook_check(ticker:str, ksi_api:str, value:dict):
    askbid:dict = {}
    last:float = 0.0
    
    try:
        if ticker == "USD" or ticker == "KRW":
            return None

        order_book:OrderBookResponseBody = ksi_function.ksi_order_book(ksi_api=ksi_api, EXCD=value.get("item_lnkg_excg_cd"), SYMB=ticker)

        current_order:dict = order_book.output1
        askbid_load:dict = order_book.output2

        
        # bid 호가 2개 ask 호가 2개
        pbid1 = to_float(askbid_load.get("pbid1"))
        pask1 = to_float(askbid_load.get("pask1"))
        pbid2 = to_float(askbid_load.get("pbid2"))
        pask2 = to_float(askbid_load.get("pask2"))

        last = to_float(current_order.get("last"))
        
        askbid[ticker] = {
            "bid1" : pbid1,
            "bid2" : pbid2,
            "ask1" : pask1,
            "ask2" : pask2
        }
    except Exception as e:
        print(e)
        traceback.print_exc()

    return askbid, last
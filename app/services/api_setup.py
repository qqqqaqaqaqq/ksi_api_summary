
from app.services.ksi_api import KSI_API

from app.models.tradeinfo import ResponseBody as TradeResponseBody
from app.models.accountinfo import ResponseBody as AccountResponseBody
from app.models.allowablemoney import ResponseBody as AllowableResponseBody
from app.models.orderbook import ResponseBody as OrderBookResponseBody
from app.models.logout import ResponseBody as LogoutResponseBody 
from app.models.order import ResponseBody as OrderResponseBody
from app.models.cancleorder import ResponseBody as CancleResponseBody
from app.models.current_balance_by_execution import ResponseBody as CBEResponseBody

# ==================
# ====== 셋팅 =======
# ==================
def ksi_api_setting(appkey, appsecret, CANO, ACNT_PRDT_CD):
    ksi_api = KSI_API(
        appkey=appkey,
        appsecret=appsecret,
        CANO=CANO,
        ACNT_PRDT_CD=ACNT_PRDT_CD,
    )

    return ksi_api

# ==================
# ===== 로그인 ======
# ==================
def ksi_login(ksi_api:KSI_API):
    request = ksi_api.login()

    return request

# ==================
# ==== 로그 아웃 ====
# ==================
def ksi_logout(ksi_api:KSI_API) -> LogoutResponseBody:
    request:dict = ksi_api.logout()

    return request.get("data")

# ==================
# ==== 거래 내역 ====
# ==================
def ksi_trade_check(ksi_api:KSI_API) -> TradeResponseBody:
    request:dict = ksi_api.get_trade_info()

    return request.get("data")

# ==================
# ==== 계좌 체크 ====
# ==================
def ksi_account_check(ksi_api:KSI_API) -> AccountResponseBody:
    request:dict = ksi_api.get_account_info()

    return request.get("data")

# ==================
# == 결제 기준 잔고 ==
# ==================
def ksi_current_balance_by_execution(ksi_api:KSI_API) -> CBEResponseBody:
    request:dict = ksi_api.current_balance_by_execution()

    return request.get("data")

# ==================
# ==== 주문 BUY ====
# ==================
def ksi_allowbale_money(ksi_api:KSI_API, OVRS_EXCG_CD:str, OVRS_ORD_UNPR:str, ITEM_CD:str) -> AllowableResponseBody:
    request:dict = ksi_api.allowable_buy_money(OVRS_EXCG_CD=OVRS_EXCG_CD, OVRS_ORD_UNPR=OVRS_ORD_UNPR , ITEM_CD=ITEM_CD)

    return request.get("data")

# ==================
# === 호가창 조회 ====
# ==================
def ksi_order_book(ksi_api:KSI_API, EXCD:str, SYMB:str) -> OrderBookResponseBody:
    request:dict = ksi_api.order_book(EXCD=EXCD, SYMB=SYMB)

    return request.get("data")

# ==================
# ====== 주문 =======
# ==================
def ksi_order(ksi_api:KSI_API, order_type:str, OVRS_EXCG_CD:str, PDNO:str, ORD_QTY:str, OVRS_ORD_UNPR:str) -> OrderResponseBody:
    request:dict = ksi_api.order(order_type=order_type, OVRS_EXCG_CD=OVRS_EXCG_CD, PDNO=PDNO, ORD_QTY=ORD_QTY, OVRS_ORD_UNPR=OVRS_ORD_UNPR)

    return request.get("data")


# ==================
# ==== 주문 취소 ====
# ==================
def ksi_cancle_order(ksi_api:KSI_API, OVRS_EXCG_CD:str, PDNO:str, ORGN_ODNO:str, ORD_QTY:str) -> CancleResponseBody:
    request:dict = ksi_api.cancle_order(OVRS_EXCG_CD, PDNO, ORGN_ODNO, ORD_QTY)

    return request.get("data")
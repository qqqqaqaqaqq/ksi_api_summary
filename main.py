import json

from app.services.ksi_api import KSI_API

from app.models.tradeinfo import ResponseBody as TradeResponseBody
from app.models.accountinfo import ResponseBody as AccountResponseBody
from app.models.allowablemoney import ResponseBody as AllowableResponseBody
from app.models.orderbook import ResponseBody as OrderBookResponseBody
from app.models.logout import ResponseBody as LogoutResponseBody 
from app.models.order import ResponseBody as OrderResponseBody
from app.models.cancleorder import ResponseBody as CancleResponseBody

import app.core.globals as globals


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

    request.get("data")

# ==================
# ==== 계좌 체크 ====
# ==================
def ksi_account_check(ksi_api:KSI_API) -> AccountResponseBody:
    request:dict = ksi_api.get_account_info()

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

# 셋팅
ksi_api = ksi_api_setting(appkey=globals.appkey, appsecret=globals.appsecret, CANO=globals.CANO, ACNT_PRDT_CD=globals.ACNT_PRDT_CD)

# 로그인
login = ksi_login(ksi_api=ksi_api)

# 트레이드 체크
trade_check = ksi_trade_check(ksi_api=ksi_api)

# 계좌 체크
account_check = ksi_account_check(ksi_api=ksi_api)

# 호가창 체크
order_book = ksi_order_book(ksi_api=ksi_api, EXCD="NAS", SYMB="APPL")

# 허용가능한 매수 금액 체크
alloable_money = ksi_allowbale_money(ksi_api=ksi_api, OVRS_EXCG_CD="NASD", OVRS_ORD_UNPR="125.0", ITEM_CD="AAPL")

# 매수
order_buy = ksi_order(ksi_api=ksi_api, order_type="TTTT1002U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORD_QTY=1, OVRS_ORD_UNPR="125.0")

# 매도
order_sell = ksi_order(ksi_api=ksi_api, order_type="TTTT1006U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORD_QTY=1, OVRS_ORD_UNPR="125.0")

uuid = order_buy.output.get("ODNO")
uuid = order_buy.output.get("ODNO")

# 주문 취소
cacle_order = ksi_cancle_order(ksi_api=ksi_api, order_tpye="TTTT1004U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORGN_ODNO=uuid, ORD_QTY="1")

print(order_book)


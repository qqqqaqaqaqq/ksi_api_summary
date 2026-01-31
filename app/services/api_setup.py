
from app.services.ksi_api import KSI_API

from app.models.tradeinfo import ResponseBody as TradeResponseBody
from app.models.accountinfo import ResponseBody as AccountResponseBody
from app.models.allowablemoney import ResponseBody as AllowableResponseBody
from app.models.orderbook import ResponseBody as OrderBookResponseBody
from app.models.logout import ResponseBody as LogoutResponseBody 
from app.models.order import ResponseBody as OrderResponseBody
from app.models.cancleorder import ResponseBody as CancleResponseBody
from app.models.current_balance_by_execution import ResponseBody as CBEResponseBody

from app.models.commonResponse import ResponseBody as ComResponseBody

# ==================
# ====== 셋팅 =======
# ==================

def _handle_response(request: ComResponseBody):
    """
    KSI_API 공통 응답 처리
    - 성공: data 반환
    - 실패: None 반환 (예외 없음)
    - 단 로그인은 엑세스 토큰 존재시 data None 반환
    """    
    if request.status == 0:
        return request.data
    else:
        # 나중에 logger로 교체 가능
        print(request.message)
        return None
    
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
    return _handle_response(ksi_api.login())

# ==================
# ==== 로그 아웃 ====
# ==================
def ksi_logout(ksi_api:KSI_API) -> LogoutResponseBody | None:
    return _handle_response(ksi_api.logout())
        
# ==================
# ==== 거래 내역 ====
# ==================
def ksi_mytrade_info(ksi_api:KSI_API) -> TradeResponseBody | None:
    return _handle_response(ksi_api.get_mystock_info())
    
# ==================
# ==== 계좌 체크 ====
# ==================
def ksi_account_check(ksi_api:KSI_API) -> AccountResponseBody | None:
    return _handle_response(ksi_api.get_account_info())
    
# ==================
# == 결제 기준 잔고 ==
# ==================
def ksi_current_balance_by_execution(ksi_api:KSI_API) -> CBEResponseBody | None:
    return _handle_response(ksi_api.current_balance_by_execution())

# ==================
# ==== 주문 BUY ====
# ==================
def ksi_allowable_money(ksi_api:KSI_API, OVRS_EXCG_CD:str, OVRS_ORD_UNPR:str, ITEM_CD:str) -> AllowableResponseBody | None:
    return _handle_response(
        ksi_api.allowable_money(OVRS_EXCG_CD=OVRS_EXCG_CD, OVRS_ORD_UNPR=OVRS_ORD_UNPR , ITEM_CD=ITEM_CD)
    )

# ==================
# === 호가창 조회 ====
# ==================
def ksi_order_book(ksi_api:KSI_API, EXCD:str, SYMB:str) -> OrderBookResponseBody | None:
    return _handle_response(
        ksi_api.order_book(EXCD=EXCD, SYMB=SYMB)
    )    
 
# ==================
# ====== 주문 =======
# ==================
def ksi_order(ksi_api:KSI_API, order_type:str, OVRS_EXCG_CD:str, PDNO:str, ORD_QTY:str, OVRS_ORD_UNPR:str) -> OrderResponseBody | None:
    return _handle_response(
        ksi_api.order(order_type=order_type, OVRS_EXCG_CD=OVRS_EXCG_CD, PDNO=PDNO, ORD_QTY=ORD_QTY, OVRS_ORD_UNPR=OVRS_ORD_UNPR)

    )

# ==================
# ==== 주문 취소 ====
# ==================
def ksi_cancel_order(ksi_api:KSI_API, OVRS_EXCG_CD:str, PDNO:str, ORGN_ODNO:str, ORD_QTY:str) -> CancleResponseBody | None:
    return _handle_response(
        ksi_api.cancel_order(OVRS_EXCG_CD, PDNO, ORGN_ODNO, ORD_QTY)
    )    

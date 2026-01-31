import requests
import traceback
import time

from datetime import datetime, timezone, timedelta

from dataclasses import asdict

from app.models.login import RequestBody as LoginRequestBody
from app.models.login import ResponseBody as LoginResponseBody

from app.models.logout import RequestBody as LogoutRequestBody
from app.models.logout import ResponseBody as LogoutResponseBody 

from app.models.tradeinfo import RequestHeader as TradeRequestHeader
from app.models.tradeinfo import RequestQueryParam as TradeRequestQueryParam
from app.models.tradeinfo import ResponseBody as TradeResponseBody

from app.models.accountinfo import RequestHeader as AccountRequestHeader
from app.models.accountinfo import RequestQueryParam as AccountRequestQueryParam
from app.models.accountinfo import ResponseBody as AccountResponseBody

from app.models.allowablemoney import RequestHeader as AllowableRequestHeader
from app.models.allowablemoney import RequestQueryParam as AllowableRequestQueryParam
from app.models.allowablemoney import ResponseBody as AllowableResponseBody

from app.models.orderbook import RequestHeader as OrderBookRequestHeader
from app.models.orderbook import RequestQueryParam as OrderBookRequestQueryParam
from app.models.orderbook import ResponseBody as OrderBookResponseBody

from app.models.order import RequestHeader as OrderRequestHeader
from app.models.order import RequestBody as OrderRequestBody
from app.models.order import ResponseBody as OrderResponseBody

from app.models.cancleorder import RequestHeader as CancleRequestHeader
from app.models.cancleorder import RequestBody as CancleRequestBody
from app.models.cancleorder import ResponseBody as CancleResponseBody

from app.models.current_balance_by_execution import RequestHeader as CBERequestHeader
from app.models.current_balance_by_execution import RequestQueryParam as CBERequestQueryParam
from app.models.current_balance_by_execution import ResponseBody as CBEResponseBody

from app.models.commonResponse import ResponseBody as ComResponseBody

# 개발
import os
import json

class KSI_API():
    def __init__(self, appkey:str, appsecret:str, CANO:str, ACNT_PRDT_CD:str):
        # 개발
        self.path = "./db.json"

        default_data = {
            "access_token": "",
            "access_token_token_expired": ""
        }

        if not os.path.exists(self.path):
            print("json 파일이 없어서 새로 생성합니다.")
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(default_data, f, ensure_ascii=False, indent=4)

        try:
            if os.path.getsize(self.path) == 0:
                raise ValueError("JSON 파일이 비어 있음")

            with open(self.path, "r", encoding="utf-8") as f:
                data: dict = json.load(f)

        except (json.JSONDecodeError, ValueError) as e:
            print(f"JSON 초기화 발생: {e}")
            data = default_data.copy()

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        self.domain:str = "https://openapi.koreainvestment.com:9443"
        self.appkey:str = appkey
        self.appsecret:str = appsecret
        self.CANO:str = CANO
        self.ACNT_PRDT_CD:str = ACNT_PRDT_CD
        self.access_token:str = data.get("access_token", "")
        self.access_token_token_expired:datetime = data.get("access_token_token_expired", "")

        # db access_token

    # ==================
    # = Expired Check ==
    # ==================
    def expired_check(self):
        if not self.access_token_token_expired:
            return False

        expired_time:datetime = datetime.fromisoformat(self.access_token_token_expired)

        expired_time_utc:datetime = (expired_time - timedelta(hours=9)).replace(tzinfo=timezone.utc)

        current_time:datetime = datetime.now(tz=timezone.utc).replace(microsecond=0)

        return expired_time_utc >= current_time

    # ==================
    # ===== 로그인 ======
    # ==================
    def login(self):
        if self.access_token:
            if self.expired_check():
                return ComResponseBody(
                    status=0,
                    http_status=200,
                    message="ALREADY_LOGGED_IN",
                    data=None
                )
            
        url = self.domain + "/oauth2/tokenP"

        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        
        data = LoginRequestBody(
            grant_type= "client_credentials",
            appkey=self.appkey,
            appsecret=self.appsecret
        )

        try:
            res = requests.post(url=url, headers=headers, json=asdict(data), timeout=10)

            body = res.json()
            response_data = LoginResponseBody(**body)
            self.access_token = response_data.access_token
            self.access_token_token_expired = response_data.access_token_token_expired
        
            # db 저장 예시         
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({
                    "access_token": response_data.access_token,
                    "access_token_token_expired": response_data.access_token_token_expired,
                }, f, ensure_ascii=False, indent=4)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="LOGIN_SUCCEEDED",
                data=res.text
            )
                        
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""                 
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"LOGIN_EXCEPTION: {str(e)} | {body_str}",
                data=None
            )            

    # ==================
    # ==== 로그 아웃 ====
    # ==================
    def logout(self):
        url = self.domain + "/oauth2/revokeP"

        if not self.access_token:
            return ComResponseBody(
                status=0,
                http_status=200,
                message="ALREADY_LOGGED_OUT",
                data=None
            )   

        headers = {
            "content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {self.access_token}"
        }
        
        data = LogoutRequestBody(
            appkey=self.appkey,
            appsecret=self.appsecret,
            token=self.access_token 
        )
                
        try:
            res = requests.post(url=url, headers=headers, json=asdict(data), timeout=10)
            self.access_token = None

            body = res.json()
            response_data = LogoutResponseBody(**body)

            default_data = {
                "access_token": "",
                "access_token_token_expired": ""
            }
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(default_data, f, ensure_ascii=False, indent=4)

            return ComResponseBody(
                status=0,
                http_status=200,
                message="LOGOUT_SUCCEEDED",
                data=response_data
            )   
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""                 
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"LOGOUT_EXCEPTION: {str(e)} | {body_str}",
                data=None
            )                  

    # ==================
    # == 나의 주식 잔고 ==
    # ==================
    def get_mystock_info(self):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/inquire-balance"

        headers = TradeRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="TTTS3012R",
            custtype="P"
        )

        params = TradeRequestQueryParam(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            OVRS_EXCG_CD="NASD",
            TR_CRCY_CD="USD",
            CTX_AREA_FK200="",
            CTX_AREA_NK200="" 
        )

        try:
            res = requests.get(url=url, params=asdict(params), headers=asdict(headers), timeout=10)
            
            body = res.json()
            response_data = TradeResponseBody(**body)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )   
            
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""                   
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[get_mystock_info]: {str(e)} | {body_str}",
                data=None
            )                  

    # ==================
    # == 결제 기준 잔고 ==
    # ==================
    def current_balance_by_execution(self):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/inquire-present-balance"

        headers = CBERequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="CTRP6504R",
            custtype="P"
        )

        params = CBERequestQueryParam(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            WCRC_FRCR_DVSN_CD="02",
            NATN_CD="000",
            TR_MKET_CD="00",
            INQR_DVSN_CD = "01"
        )

        try:
            res = requests.get(url=url, params=asdict(params), headers=asdict(headers), timeout=10)
            
            body = res.json()
            response_data = CBEResponseBody(**body)
            

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )   
            
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""            
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[current_balance_by_execution]: {str(e)} | {body_str}",
                data=None
            )   
        
    # ==================
    # == 계좌 잔고 조회 ==
    # ==================
    def get_account_info(self):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")            
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/inquire-paymt-stdr-balance"

        # tr_id 고정
        headers = AccountRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="CTRP6010R",
            tr_cont="",
            custtype="P"
        )

        params = AccountRequestQueryParam(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            BASS_DT=datetime.now().strftime("%Y%m%d"),
            WCRC_FRCR_DVSN_CD="02",
            INQR_DVSN_CD="01"
        )

        try:
            res = requests.get(url=url, params=asdict(params), headers=asdict(headers), timeout=10)
            
            body = res.json()
            response_data = AccountResponseBody(**body)

            response_data.output1
            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )   
            
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[get_account_info]: {str(e)} | {body_str}",
                data=None
            )   
        
    # ==================
    # == 매수 가능 금액 ==
    # ==================
    def allowable_money(self, OVRS_EXCG_CD:str, OVRS_ORD_UNPR:str, ITEM_CD:str):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")            
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/inquire-psamount"
	
        # tr_id 고정
        headers = AllowableRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="TTTS3007R",
            tr_cont="",
            custtype="P"
        )

        params = AllowableRequestQueryParam(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            OVRS_EXCG_CD=OVRS_EXCG_CD,
            OVRS_ORD_UNPR=OVRS_ORD_UNPR,
            ITEM_CD=ITEM_CD,
        )

        try:
            res = requests.get(url=url, params=asdict(params), headers=asdict(headers), timeout=10)
            
            body = res.json()
            
            response_data = AllowableResponseBody(**body)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )   
        
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""
            traceback.print_exc()    
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[allowable_buy_money]: {str(e)} | {body_str}",
                data=None
            ) 
            
    # ==================
    # ===== 호가창 ======
    # ==================
    def order_book(self, EXCD:str, SYMB:str):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")                 
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-price/v1/quotations/inquire-asking-price"
	
        # tr_id 고정
        headers = OrderBookRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="HHDFS76200100",
            tr_cont="",
            custtype="P"
        )

        params = OrderBookRequestQueryParam(
            AUTH="",
            EXCD=EXCD,
            SYMB=SYMB
        )

        try:
            res = requests.get(url=url, params=asdict(params), headers=asdict(headers), timeout=10)
            
            body = res.json()
            
            response_data = OrderBookResponseBody(**body)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )  
        
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""
            traceback.print_exc()    
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[order_book]: {str(e)} | {body_str}",
                data=None
            ) 
        
    # ==================
    # ====== 주문 =======
    # ==================
    def order(self, order_type:str, OVRS_EXCG_CD:str, PDNO:str, ORD_QTY:str, OVRS_ORD_UNPR:str):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")                     
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/order"
	
        headers = OrderRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id=order_type,
            tr_cont="",
            custtype="P"
        )

        data = OrderRequestBody(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            OVRS_EXCG_CD=OVRS_EXCG_CD,
            PDNO=PDNO,
            ORD_QTY=str(ORD_QTY),
            OVRS_ORD_UNPR=str(OVRS_ORD_UNPR),
            SLL_TYPE="00" if order_type=="TTTT1006U" else "",
            ORD_DVSN="00",
            ORD_SVR_DVSN_CD="0"
        )

        try:
            res = requests.post(url=url, headers=asdict(headers), json=asdict(data), timeout=10)
            
            body = res.json()
            
            response_data = OrderResponseBody(**body)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )  
            
        except Exception as e:
            traceback.print_exc()
            body_str = f" | {body}" if 'body' in locals() else ""

            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[order]: {str(e)} | {body_str}",
                data=None
            )             

    # ==================
    # ==== 주문 취소 ====
    # ==================
    def cancel_order(self, OVRS_EXCG_CD:str, PDNO:str, ORGN_ODNO:str, ORD_QTY:str):
        if not self.access_token:
            self.login()

        if not self.expired_check():
            print("토큰 만료 재 로그인 합니다.")                   
            self.logout()
            time.sleep(2)
            self.login()
  
        url = self.domain + "/uapi/overseas-stock/v1/trading/order-rvsecncl"
	
        headers = CancleRequestHeader(
            content_type="application/json; charset=utf-8",
            authorization = f"Bearer {self.access_token}",
            appkey=self.appkey,
            appsecret=self.appsecret,
            tr_id="TTTT1004U",
            tr_cont="",
            custtype="P"
        )

        data = CancleRequestBody(
            CANO=self.CANO,
            ACNT_PRDT_CD=self.ACNT_PRDT_CD,
            OVRS_EXCG_CD=OVRS_EXCG_CD,
            PDNO=PDNO,
            ORGN_ODNO=ORGN_ODNO,
            RVSE_CNCL_DVSN_CD="02",
            ORD_QTY = ORD_QTY,
            OVRS_ORD_UNPR="0",
        )

        try:
            res = requests.post(url=url, headers=asdict(headers), json=asdict(data), timeout=10)
            
            body = res.json()

            response_data = CancleResponseBody(**body)

            return ComResponseBody(
                status=0,
                http_status=res.status_code,
                message="INQUIRY_SUCCEEDED",
                data=response_data
            )  
            
        except Exception as e:
            body_str = f" | {body}" if 'body' in locals() else ""
            traceback.print_exc()
            return ComResponseBody(
                status=9001,
                http_status=None,
                message=f"[cancle_order]: {str(e)} | {body_str}",
                data=None
            )                    
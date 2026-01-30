# Ksi API Documnents Command File

# 필수 파일
.env

appkey=*****<br>
appsecret=*****<br>

CANO=*****<br>
ACNT_PRDT_CD=*****<br>

--- 

## 셋팅
ksi_api = ksi_api_setting(appkey=globals.appkey, appsecret=globals.appsecret, CANO=globals.CANO, ACNT_PRDT_CD=globals.ACNT_PRDT_CD)

## 로그인
login = ksi_login(ksi_api=ksi_api)

## 트레이드 체크
trade_check = ksi_trade_check(ksi_api=ksi_api)

## 계좌 체크
account_check = ksi_account_check(ksi_api=ksi_api)

## 호가창 체크
order_book = ksi_order_book(ksi_api=ksi_api, EXCD="NAS", SYMB="APPL")

## 허용가능한 매수 금액 체크
alloable_money = ksi_allowbale_money(ksi_api=ksi_api, OVRS_EXCG_CD="NASD", OVRS_ORD_UNPR="125.0", ITEM_CD="AAPL")

## 매수
order_buy = ksi_order(ksi_api=ksi_api, order_type="TTTT1002U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORD_QTY=1, OVRS_ORD_UNPR="125.0")

## 매도
order_sell = ksi_order(ksi_api=ksi_api, order_type="TTTT1006U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORD_QTY=1, OVRS_ORD_UNPR="125.0")

## 주문 번호
uuid = order_buy.output.get("ODNO")
uuid = order_buy.output.get("ODNO")

## 주문 취소
cacle_order = ksi_cancle_order(ksi_api=ksi_api, order_tpye="TTTT1004U", OVRS_EXCG_CD="NASD", PDNO="AAPL", ORGN_ODNO=uuid, ORD_QTY="1")

--- 

따로 사용하는 DB 있으면 db.json => db host로 변경
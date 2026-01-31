# Ksi API Documnents Command File

# Update
- work_flow
- ksi command Mixed
  - app.services.api_setup : 한줄 커맨드
  - app.services.orderbook_check : 오더북 상단 비드 2개 하단 ask 2개 반환
  - app.services.summary_ticker : 현재 티커 요약, USD,KRW는 예금액만
  - app.services.order_service : ask, bid 기준 매수 현재가 대비 위험 스프레드 (현재가와 오더북 차이가 1% 차이시 오더 금지)

- 내부 성공 
  - status = 0 
- 외부 api 성공
  - http_status = 0
  - 없으면 None
 
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
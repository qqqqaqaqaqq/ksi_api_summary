import traceback

import app.core.globals as globals

import app.services.api_setup as ksi_function

from app.services.summary_ticker import summary_ticker
from app.services.orderbook_check import orderbook_check
from app.services.order_service import order
from app.models.current_balance_by_execution import ResponseBody as CBEResponseBody
from app.models.commonResponse import ResponseBody as ComResponseBody

# work_flow
def work_flow():
    try:
        # 셋팅    
        ksi_api = ksi_function.ksi_api_setting(appkey=globals.appkey, appsecret=globals.appsecret, CANO=globals.CANO, ACNT_PRDT_CD=globals.ACNT_PRDT_CD)

        # 로그인
        login = ksi_function.ksi_login(ksi_api=ksi_api)
        print(f"login : {login}")

 
        # 계좌 잔고 조회
        current_balance_by_execution:CBEResponseBody | None = ksi_function.ksi_current_balance_by_execution(ksi_api=ksi_api)
        
        ksi_account_check =  ksi_function.ksi_account_check(ksi_api=ksi_api)
        ksi_mytrade_info = ksi_function.ksi_mytrade_info(ksi_api=ksi_api)

        account_stock_data:list[dict] = current_balance_by_execution.output1
        account_avaliable_data:list[dict] = current_balance_by_execution.output2

        summary:dict[str, dict] = {}

        for data in account_stock_data:
            response:ComResponseBody = summary_ticker(data)

            if response.status != 0:
                print(response)
                continue

            summary.update(response.data)

        for data in account_avaliable_data:
            response:ComResponseBody = summary_ticker(data)

            if response.status != 0:
                print(response)
                continue

            summary.update(response.data)

        print(summary)

        # {
        #     "USD": {
        #         "available_cash": 138.72
        #     },
        #     "GOOG": {
        #         "item_lnkg_excg_cd": "NAS",     # 연계 거래소 (나스닥)
        #         "ovrs_excg_cd": "NASD",          # 해외 거래소 코드
        #         "avg_price": 132.45,             # 평균 매수가
        #         "quantity": 3.0,                 # 보유 수량
        #         "current_profit_rate": 4.82,     # 수익률 (%)
        #         "ovrs_now_pric1": 138.83         # 현재가
        #     }
        # }

        # key : USD, GOOG
        # value 

        # EXCD = value.get("item_lnkg_excg_cd")
        EXCD = "NAS"
        ticker = "AAPL"
        orderbook:ComResponseBody = orderbook_check(ticker, ksi_api=ksi_api, EXCD=EXCD)
        print(orderbook)

        orderbook_data:dict =orderbook.data

        # EXCD = value.get("ovrs_excg_cd")
        EXCD = "NASD"
        order_type = "TTTT1002U"
        uuid:ComResponseBody = order(
            order_type=order_type, 
            ksi_api=ksi_api,
            ticker=orderbook_data.get("ticker"),
            EXCD=EXCD, 
            askbid=orderbook_data.get("askbid"),
            last=orderbook_data.get("last")
        )

        print(uuid)

        # 로그 아웃
        # ksi_logout = ksi_function.ksi_logout(ksi_api=ksi_api)
    except Exception as e:
        print(e)
        traceback.print_exc()
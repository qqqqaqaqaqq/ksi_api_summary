import json
import traceback

import app.core.globals as globals

import app.services.api_setup as ksi_function

from app.services.summary_ticker import summary_ticker
from app.models.current_balance_by_execution import ResponseBody as CBEResponseBody


# work_flow
def work_flow():
    try:
        # 셋팅    
        ksi_api = ksi_function.ksi_api_setting(appkey=globals.appkey, appsecret=globals.appsecret, CANO=globals.CANO, ACNT_PRDT_CD=globals.ACNT_PRDT_CD)

        # 로그인
        login = ksi_function.ksi_login(ksi_api=ksi_api)
        print(f"login : {login}")

        # 계좌 잔고 조회
        current_balance_by_execution:CBEResponseBody = ksi_function.ksi_current_balance_by_execution(ksi_api=ksi_api)

        account_stock_data:list[dict] = current_balance_by_execution.output1
        account_avaliable_data:list[dict] = current_balance_by_execution.output2

        summary:dict[str, dict] = {}

        for data in account_stock_data:
            summary.update(summary_ticker(data))

        for data in account_avaliable_data:
            summary.update(summary_ticker(data))
        
        order_type = "TTTT1006U"
    except Exception as e:
        print(e)
        traceback.print_exc()
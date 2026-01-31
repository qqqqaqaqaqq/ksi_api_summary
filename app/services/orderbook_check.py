import traceback

import app.services.api_setup as ksi_function
from app.models.orderbook import ResponseBody as OrderBookResponseBody
from app.models.commonResponse import ResponseBody as ComResponseBody
from app.services.utils import to_float

# ==================
# ==== 오더북 조회 ====
# ==================
def orderbook_check(ticker: str, ksi_api: str, EXCD: str) -> ComResponseBody:
    try:
        # 통화는 오더북 조회 대상 아님
        if ticker in ("USD", "KRW"):
            return ComResponseBody(
                status=1000,
                http_status=None,
                message="CURRENCY_SKIP",
                data=None
            )

        # 오더북 조회
        order_book: OrderBookResponseBody = ksi_function.ksi_order_book(
            ksi_api=ksi_api,
            EXCD=EXCD,
            SYMB=ticker
        )

        if not order_book:
            return ComResponseBody(
                status=1002,
                http_status=None,
                message="ORDERBOOK_EMPTY",
                data=None
            )

        # 체결 정보 / 호가 정보
        execution_info: dict = order_book.output1
        orderbook_info: dict = order_book.output2

        # 현재가
        last_price = to_float(execution_info.get("last"))

        # 1·2차 매수/매도 호가
        askbid = {
            "bid1": to_float(orderbook_info.get("pbid1")),
            "bid2": to_float(orderbook_info.get("pbid2")),
            "ask1": to_float(orderbook_info.get("pask1")),
            "ask2": to_float(orderbook_info.get("pask2")),
        }

        return ComResponseBody(
            status=0,
            http_status=None,
            message="ORDERBOOK_OK",
            data={
                "ticker": ticker,
                "askbid": askbid,
                "last": last_price
            }
        )

    except Exception as e:
        print(e)
        traceback.print_exc()
        return ComResponseBody(
            status=9001,
            http_status=None,
            message=f"[orderbook_check] {str(e)}",
            data=None
        )

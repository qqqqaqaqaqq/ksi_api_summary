from dataclasses import dataclass
from typing import Optional

@dataclass
class RequestHeader:
    authorization: str    #접근토큰
    appkey: str    #앱키
    appsecret: str    #앱시크릿키   
    tr_id: str    #거래ID     
    content_type: Optional[str] = None    #컨텐츠타입
    personalseckey: Optional[str] = None    #고객식별키
    tr_cont: Optional[str] = None    #연속 거래 여부
    custtype: Optional[str] = None    #고객 타입
    seq_no: Optional[str] = None    #일련번호
    mac_address: Optional[str] = None    #맥주소
    phone_number: Optional[str] = None    #핸드폰번호
    ip_addr: Optional[str] = None    #접속 단말 공인 IP
    gt_uid: Optional[str] = None    #Global UID

@dataclass
class RequestQueryParam:
    CANO: str    #종합계좌번호
    ACNT_PRDT_CD: str    #계좌상품코드
    OVRS_EXCG_CD: str    #해외거래소코드
    OVRS_ORD_UNPR: str    #해외주문단가
    ITEM_CD: str    #종목코드

@dataclass
class ResponseBodyoutput:
    tr_crcy_cd: Optional[str] = None    #거래통화코드
    ord_psbl_frcr_amt: Optional[str] = None    #주문가능외화금액
    sll_ruse_psbl_amt: Optional[str] = None    #매도재사용가능금액
    ovrs_ord_psbl_amt: Optional[str] = None    #해외주문가능금액
    max_ord_psbl_qty: Optional[str] = None    #최대주문가능수량
    echm_af_ord_psbl_amt: Optional[str] = None    #환전이후주문가능금액
    echm_af_ord_psbl_qty: Optional[str] = None    #환전이후주문가능수량
    ord_psbl_qty: Optional[str] = None    #주문가능수량
    exrt: Optional[str] = None    #환율
    frcr_ord_psbl_amt1: Optional[str] = None    #외화주문가능금액1
    ovrs_max_ord_psbl_qty: Optional[str] = None    #해외최대주문가능수량

@dataclass
class ResponseHeader:
    content_type: str    #컨텐츠타입
    tr_id: str    #거래ID
    tr_cont: Optional[str] = None    #연속 거래 여부
    gt_uid: Optional[str] = None    #Global UID

@dataclass
class ResponseBody:
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output: Optional[ResponseBodyoutput] = None    #응답상세1


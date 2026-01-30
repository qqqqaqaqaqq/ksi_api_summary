from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class RequestHeader:
    authorization: str    #접근토큰
    appkey: str    #앱키 
    appsecret: str    #앱시크릿키
    tr_id: str    #거래ID
    content_type: Optional[str] = None    #컨텐츠타입    
    personalseckey: Optional[str] = None    #고객식별키    
    tr_cont: Optional[str] = None    #연속 거래 여부
    custtype: Optional[str] = None    #고객타입
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
    TR_CRCY_CD: str    #거래통화코드
    CTX_AREA_FK200: Optional[str] = None    #연속조회검색조건200
    CTX_AREA_NK200: Optional[str] = None    #연속조회키200

@dataclass
class ResponseHeader:
    content_type: str    #컨텐츠타입
    tr_id: str    #거래ID
    tr_cont: str    #연속 거래 여부
    gt_uid: str    #Global UID

@dataclass
class ResponseBodyoutput1:
    cano: str    #종합계좌번호
    acnt_prdt_cd: str    #계좌상품코드
    prdt_type_cd: str    #상품유형코드
    ovrs_pdno: str    #해외상품번호
    ovrs_item_name: str    #해외종목명
    frcr_evlu_pfls_amt: str    #외화평가손익금액
    evlu_pfls_rt: str    #평가손익율
    pchs_avg_pric: str    #매입평균가격
    ovrs_cblc_qty: str    #해외잔고수량
    ord_psbl_qty: str    #주문가능수량
    frcr_pchs_amt1: str    #외화매입금액1
    ovrs_stck_evlu_amt: str    #해외주식평가금액
    now_pric2: str    #현재가격2
    tr_crcy_cd: str    #거래통화코드
    ovrs_excg_cd: str    #해외거래소코드
    loan_type_cd: str    #대출유형코드
    loan_dt: str    #대출일자
    expd_dt: str    #만기일자

@dataclass
class ResponseBodyoutput2:
    frcr_pchs_amt1: str    #외화매입금액1
    ovrs_rlzt_pfls_amt: str    #해외실현손익금액
    ovrs_tot_pfls: str    #해외총손익
    rlzt_erng_rt: str    #실현수익율
    tot_evlu_pfls_amt: str    #총평가손익금액
    tot_pftrt: str    #총수익률
    frcr_buy_amt_smtl1: str    #외화매수금액합계1
    ovrs_rlzt_pfls_amt2: str    #해외실현손익금액2
    frcr_buy_amt_smtl2: str    #외화매수금액합계2

@dataclass
class ResponseBody:
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    ctx_area_fk200: str =None   #연속조회검색조건200
    ctx_area_nk200: str = None   #연속조회키200
    output1: List[ResponseBodyoutput1] = field(default_factory=list)    #응답상세1    
    output2: ResponseBodyoutput2 =None   #응답상세2    

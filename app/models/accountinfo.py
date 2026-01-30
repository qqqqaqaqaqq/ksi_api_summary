from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class RequestHeader:
    content_type: str    #컨텐츠타입
    authorization: str    #접근토큰
    appkey: str    #앱키
    appsecret: str    #앱시크릿키
    tr_id: str    #거래ID
    custtype: str    #고객 타입    
    personalseckey: Optional[str] = None    #고객식별키
    tr_cont: Optional[str] = None    #연속 거래 여부
    seq_no: Optional[str] = None    #일련번호
    mac_address: Optional[str] = None    #맥주소
    phone_number: Optional[str] = None    #핸드폰번호
    ip_addr: Optional[str] = None    #접속 단말 공인 IP
    gt_uid: Optional[str] = None    #Global UID

@dataclass
class RequestQueryParam:
    CANO: str    #종합계좌번호
    ACNT_PRDT_CD: str    #계좌상품코드
    BASS_DT: str    #기준일자
    WCRC_FRCR_DVSN_CD: str    #원화외화구분코드
    INQR_DVSN_CD: str    #조회구분코드

@dataclass
class ResponseHeader:
    content_type: str    #컨텐츠타입
    tr_id: str    #거래ID
    tr_cont: Optional[str] = None    #연속 거래 여부
    gt_uid: Optional[str] = None    #Global UID

@dataclass
class ResponseBodyoutput1:
    pdno: str    #상품번호
    prdt_name: str    #상품명
    cblc_qty13: str    #잔고수량13
    ord_psbl_qty1: str    #주문가능수량1
    avg_unpr3: str    #평균단가3
    ovrs_now_pric1: str    #해외현재가격1
    frcr_pchs_amt: str    #외화매입금액
    frcr_evlu_amt2: str    #외화평가금액2
    evlu_pfls_amt2: str    #평가손익금액2
    bass_exrt: str    #기준환율
    oprt_dtl_dtime: str    #조작상세일시
    buy_crcy_cd: str    #매수통화코드
    thdt_sll_ccld_qty1: str    #당일매도체결수량1
    thdt_buy_ccld_qty1: str    #당일매수체결수량1
    evlu_pfls_rt1: str    #평가손익율1
    tr_mket_name: str    #거래시장명
    natn_kor_name: str    #국가한글명
    std_pdno: str    #표준상품번호
    mgge_qty: str    #담보수량
    loan_rmnd: str    #대출잔액
    prdt_type_cd: str    #상품유형코드
    ovrs_excg_cd: str    #해외거래소코드
    scts_dvsn_name: str    #유가증권구분명
    ldng_cblc_qty: str    #대여잔고수량

@dataclass
class ResponseBodyoutput2:
    crcy_cd: str    #통화코드
    crcy_cd_name: str    #통화코드명
    frcr_dncl_amt_2: str    #외화예수금액2
    frst_bltn_exrt: str    #최초고시환율
    frcr_evlu_amt2: str    #외화평가금액2

@dataclass
class ResponseBodyoutput3:
    pchs_amt_smtl_amt: str    #매입금액합계금액
    tot_evlu_pfls_amt: str    #총평가손익금액
    evlu_erng_rt1: str    #평가수익율1
    tot_dncl_amt: str    #총예수금액
    wcrc_evlu_amt_smtl: str    #원화평가금액합계
    tot_asst_amt2: str    #총자산금액2
    frcr_cblc_wcrc_evlu_amt_smtl: str    #외화잔고원화평가금액합계
    tot_loan_amt: str    #총대출금액
    tot_ldng_evlu_amt: str    #총대여평가금액

@dataclass
class ResponseBody:
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output1: List[ResponseBodyoutput1] = field(default_factory=list)    #응답상세
    output2: List[ResponseBodyoutput2] = field(default_factory=list)    #응답상세
    output3: ResponseBodyoutput3 = None   #응답상세

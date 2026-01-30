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
    AUTH: str    #사용자권한정보
    EXCD: str    #거래소코드
    SYMB: str    #종목코드

@dataclass
class ResponseHeader:
    content_type: str    #컨텐츠타입
    tr_id: str    #거래ID
    tr_cont: Optional[str] = None    #연속 거래 여부
    gt_uid: Optional[str] = None    #Global UID

@dataclass
class ResponseBodyoutput1:
    rsym: str    #실시간조회종목코드
    zdiv: str    #소수점자리수
    curr: str    #통화
    base: str    #전일종가
    open: str    #시가
    high: str    #고가
    low: str    #저가
    last: str    #현재가
    dymd: str    #호가일자
    dhms: str    #호가시간
    bvol: str    #매수호가총잔량
    avol: str    #매도호가총잔량
    bdvl: str    #매수호가총잔량대비
    advl: str    #매도호가총잔량대비
    code: str    #종목코드
    ropen: str    #시가율
    rhigh: str    #고가율
    rlow: str    #저가율
    rclose: str    #현재가율

@dataclass
class ResponseBodyoutput2:
    pbid1: str    #매수호가가격1
    pask1: str    #매도호가가격1
    vbid1: str    #매수호가잔량1
    vask1: str    #매도호가잔량1
    dbid1: str    #매수호가대비1
    dask1: str    #매도호가대비1
    pbid2: str    #매수호가가격2
    pask2: str    #매도호가가격2
    vbid2: str    #매수호가잔량2
    vask2: str    #매도호가잔량2
    dbid2: str    #매수호가대비2
    dask2: str    #매도호가대비2
    pbid3: str    #매수호가가격3
    pask3: str    #매도호가가격3
    vbid3: str    #매수호가잔량3
    vask3: str    #매도호가잔량3
    dbid3: str    #매수호가대비3
    dask3: str    #매도호가대비3
    pbid4: str    #매수호가가격4
    pask4: str    #매도호가가격4
    vbid4: str    #매수호가잔량4
    vask4: str    #매도호가잔량4
    dbid4: str    #매수호가대비4
    dask4: str    #매도호가대비4
    pbid5: str    #매수호가가격5
    pask5: str    #매도호가가격5
    vbid5: str    #매수호가잔량5
    vask5: str    #매도호가잔량5
    dbid5: str    #매수호가대비5
    dask5: str    #매도호가대비5
    pbid6: str    #매수호가가격6
    pask6: str    #매도호가가격6
    vbid6: str    #매수호가잔량6
    vask6: str    #매도호가잔량6
    dbid6: str    #매수호가대비6
    dask6: str    #매도호가대비6
    pbid7: str    #매수호가가격7
    pask7: str    #매도호가가격7
    vbid7: str    #매수호가잔량7
    vask7: str    #매도호가잔량7
    dbid7: str    #매수호가대비7
    dask7: str    #매도호가대비7
    pbid8: str    #매수호가가격8
    pask8: str    #매도호가가격8
    vbid8: str    #매수호가잔량8
    vask8: str    #매도호가잔량8
    dbid8: str    #매수호가대비8
    dask8: str    #매도호가대비8
    pbid9: str    #매수호가가격9
    pask9: str    #매도호가가격9
    vbid9: str    #매수호가잔량9
    vask9: str    #매도호가잔량9
    dbid9: str    #매수호가대비9
    dask9: str    #매도호가대비9
    pbid10: str    #매수호가가격10
    pask10: str    #매도호가가격10
    vbid10: str    #매수호가잔량10
    vask10: str    #매도호가잔량10
    dbid10: str    #매수호가대비10
    dask10: str    #매도호가대비10

@dataclass
class ResponseBodyoutput3:
    vstm: str    #VCMStart시간
    vetm: str    #VCMEnd시간
    csbp: str    #CAS/VCM기준가
    cshi: str    #CAS/VCMHighprice
    cslo: str    #CAS/VCMLowprice
    iep: str    #IEP
    iev: str    #IEV


@dataclass
class ResponseBody:
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output1: ResponseBodyoutput1    #응답상세
    output2: List[ResponseBodyoutput2] = field(default_factory=list)    #응답상세
    output3: List[ResponseBodyoutput3] = field(default_factory=list)    #응답상세

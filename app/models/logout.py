from dataclasses import dataclass
from typing import Optional

@dataclass
class RequestBody:
    appkey: str
    appsecret: str
    token: str

@dataclass
class ResponseBody:
    code: Optional[str] = None
    message: Optional[str] = None
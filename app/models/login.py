from dataclasses import dataclass

@dataclass
class RequestBody:
    grant_type: str
    appkey: str
    appsecret: str

@dataclass
class ResponseBody:
    access_token: StopAsyncIteration
    token_type: str
    expires_in: float
    access_token_token_expired: str 
from dataclasses import dataclass
from typing import Any

@dataclass
class ResponseBody():
    status : int
    http_status: int
    message : str
    data : Any
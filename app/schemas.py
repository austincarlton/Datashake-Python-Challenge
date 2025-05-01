from pydantic import BaseModel
from typing import List, Optional

class SignupResponse(BaseModel):
    api_key: str
    credits: int

class ConvertRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    date: Optional[str] = None  # format YYYY-MM-DD

class ConvertResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    converted: float
    rate: float
    date: str

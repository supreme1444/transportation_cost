from datetime import date
from pydantic import BaseModel


class InsuranceRequest(BaseModel):
    date_request: date
    cargo_type: str
    declared_value: float


class InsuranceResponse(BaseModel):
    cost: float

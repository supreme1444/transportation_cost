from datetime import datetime

from pydantic import BaseModel


class InsuranceRequest(BaseModel):
    date_request: datetime
    cargo_type: str
    declared_value: float


class InsuranceResponse(BaseModel):
    cost: float


class EditRateRequest(BaseModel):
    id: int
    rate: float
    cargo_type: str


class EditRateResponse(BaseModel):
    cargo_type: str
    rate: float


class AddRateRequest(BaseModel):
    id: int


class AddRateRespons(BaseModel):
    message: str

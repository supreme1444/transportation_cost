from datetime import  date
from pydantic import BaseModel


class InsuranceRequest(BaseModel):
    date_request: date
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


class DeleteRateRequest(BaseModel):
    id: int


class DeleteRateRespons(BaseModel):
    message: str


class AddRateRequest(BaseModel):
    date_request: date
    cargo_type: str
    rate: float


class AddRateRespons(BaseModel):
    message: str

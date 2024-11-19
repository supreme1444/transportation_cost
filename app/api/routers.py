from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.schemas_tariff import InsuranceRequest, InsuranceResponse
from app.database.database import get_db
from app.services.services import calculate_insurance_cost

router = APIRouter()


@router.post("/calculate-insurance/", response_model=InsuranceResponse)
async def calculate_insurance(request: InsuranceRequest, db: AsyncSession = Depends(get_db)):
    """
    Асинхронный эндпоинт для расчета стоимости страховки.
    """
    try:
        cost = await calculate_insurance_cost(db, request.date_request, request.cargo_type, request.declared_value)
        return InsuranceResponse(cost=cost)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

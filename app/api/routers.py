from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.schemas_tariff import (InsuranceRequest, InsuranceResponse,
                                        EditRateResponse, AddRateRequest,
                                        EditRateRequest, AddRateRespons)
from app.database.database import get_db
from app.services.services import calculate_insurance_cost, edit_insurance_services, delete_rate_services

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


@router.delete("/edit-insurance/", response_model=EditRateResponse)
async def edit_insurance(request: EditRateRequest, db: AsyncSession = Depends(get_db)):
    """
        Асинхронный эндпоинт для редактирования тарифа.
    """
    try:
        edit = await edit_insurance_services(db, request.id, request.rate, request.cargo_type)
        return edit
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/delete-rate/", response_model=AddRateRespons)
async def add_rate(request: AddRateRequest, db: AsyncSession = Depends(get_db)):
    """
        Асинхронный эндпоинт для удаления тарифа.
    """
    try:
        await delete_rate_services(db, request.id)
        return {
            "message": "Тариф успешно удален."
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

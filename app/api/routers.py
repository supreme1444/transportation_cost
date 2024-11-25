from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.schemas_tariff import (InsuranceRequest, InsuranceResponse,
                                        EditRateResponse,
                                        EditRateRequest, DeleteRateRespons, DeleteRateRequest, AddRateRespons,
                                        AddRateRequest, )
from app.database.database import get_db
from app.services.services import calculate_insurance_cost, edit_insurance_services, delete_rate_services, \
    add_rate_services

router = APIRouter()


@router.post("/calculate-insurance/", response_model=InsuranceResponse)
async def calculate_insurance(request: InsuranceRequest, db: AsyncSession = Depends(get_db)):
    """
    Асинхронный эндпоинт для расчета стоимости страховки.
    Введите дату "date_request-2022-03-10"
    Тип груза "cargo_type-Clothing"
    Стоимость груза "declared_value-40000".
    """
    try:
        cost = await calculate_insurance_cost(db, request.date_request, request.cargo_type, request.declared_value)
        return InsuranceResponse(cost=cost)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/edit-rate/", response_model=EditRateResponse)
async def edit_rate(request: EditRateRequest, db: AsyncSession = Depends(get_db)):
    """
    Асинхронный эндпоинт для редактирования тарифа.
    Введите id тарифа "id-3"и отредактируйте его условия.
    Тариф "rate-0.03"
    Тип груза "cargo_type-Clothing"
    """
    try:
        edit = await edit_insurance_services(db, request.id, request.rate, request.cargo_type)
        return edit
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/delete-rate/", response_model=DeleteRateRespons)
async def delete_rate(request: DeleteRateRequest, db: AsyncSession = Depends(get_db)):
    """
    Асинхронный эндпоинт для удаления тарифа.
    Введите id тарифа, который хотите удалить.
    """
    try:
        result = await delete_rate_services(db, request.id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/add-rate/", response_model=AddRateRespons)
async def add_rate(request: AddRateRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await add_rate_services(db, request.date_request, request.cargo_type, request.rate)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_rate, edit_insurance_rate, delete_insurance_rate, add_insurance_rate


async def calculate_insurance_cost(db: AsyncSession, date: datetime, cargo_type: str, declared_value: float) -> float:
    rate = await get_rate(db, date, cargo_type)
    if not rate:
        raise ValueError("Тариф не найден")
    return declared_value * rate.rate


async def edit_insurance_services(db: AsyncSession, id_rate: int, new_edit_rate: float, new_edit_cargo: str):
    edited_tariff = await edit_insurance_rate(db, id_rate, new_edit_rate, new_edit_cargo)
    if not edited_tariff:
        raise ValueError("Тариф не найден")
    return edited_tariff


async def delete_rate_services(db: AsyncSession, id_rate: int):
    delete_rate = await delete_insurance_rate(db, id_rate)
    if not delete_rate:
        raise ValueError("Тариф не найден")
    return delete_rate


async def add_rate_services(db: AsyncSession, date_request: datetime, cargo: str, rate: float):
    add_rate = await add_insurance_rate(db, date_request, cargo, rate)
    if not add_rate:
        raise ValueError("Тариф не найден")
    return add_rate

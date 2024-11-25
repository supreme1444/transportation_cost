from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_rate, edit_insurance_rate, delete_insurance_rate

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
    result = await delete_insurance_rate(db, id_rate)
    return result

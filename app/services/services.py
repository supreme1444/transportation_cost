from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_rate, edit_insurance_rate, delete_insurance_rate, add_insurance_rate


async def calculate_insurance_cost(db: AsyncSession, date: datetime, cargo_type: str, declared_value: float) -> float:
    rate = await get_rate(db, date, cargo_type)
    """
    Асинхронный эндпоинт для расчета стоимости страховки.
    """
    if not rate:
        raise ValueError("Тариф не найден")
    return declared_value * rate.rate


async def edit_insurance_services(db: AsyncSession, id: int, new_edit_rate: float, new_edit_cargo: str):
    """
    Функция для редактирования страховых услуг.
    """
    edited_tariff = await edit_insurance_rate(db, id, new_edit_rate, new_edit_cargo)
    if not edited_tariff:
        raise ValueError("Тариф не найден")
    return edited_tariff


async def delete_rate_services(db: AsyncSession, id: int):
    """
    Функция для удаления страховых услуг.
    """
    delete_rate = await delete_insurance_rate(db, id)
    if not delete_rate:
        raise ValueError("Тариф не найден")
    return delete_rate


async def add_rate_services(db: AsyncSession, date_request: datetime, cargo: str, rate: float):
    add_rate = await add_insurance_rate(db, date_request, cargo, rate)
     """
    Функция для добавления страховых услуг.
    """
    if not add_rate:
        raise ValueError("Тариф не найден")
    return add_rate

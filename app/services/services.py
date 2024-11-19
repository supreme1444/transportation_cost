from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud import get_rate


async def calculate_insurance_cost(db: AsyncSession, date: datetime, cargo_type: str, declared_value: float) -> float:
    rate = await get_rate(db, date, cargo_type)

    if not rate:
        raise ValueError("Тариф не найден")
    return declared_value * rate.rate

from datetime import datetime

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models_tariff import Tariff


async def get_rate(db: AsyncSession, date: datetime, cargo_type: str):
    result = await db.execute(
        select(Tariff).where(Tariff.date == date, Tariff.cargo_type == cargo_type)
    )
    return result.scalar_one_or_none()

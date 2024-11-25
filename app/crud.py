from datetime import datetime

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models_tariff import Tariff
from logger import log_event


async def get_rate(db: AsyncSession, date: datetime, cargo_type: str):
    result = await db.execute(
        select(Tariff).where(Tariff.date == date.date(), Tariff.cargo_type == cargo_type)
    )
    log_event(
        user_id=None,
        action=f"Получение тарифа для типа груза '{cargo_type}' на дату {date.date().isoformat()}",
        timestamp=datetime.utcnow().date().isoformat()
    )
    return result.scalar_one_or_none()


async def get_id_rate(db: AsyncSession, id: int):
    """
    Получение тарифа по ID.
    """
    result = await db.execute(select(Tariff).filter_by(id=id))
    return result.scalar_one_or_none()


async def edit_insurance_rate(db: AsyncSession, id: int, new_edit_rate: float, new_edit_cargo: str):
    tariff = await get_id_rate(db, id)
    if not tariff:
        raise ValueError("Тариф не найден")
    tariff.rate = new_edit_rate
    tariff.cargo_type = new_edit_cargo
    log_event(
        user_id=None,
        action=f"Редактирование тарифа ID {id}: новый тариф {new_edit_rate}, новый тип груза {new_edit_cargo}",
        timestamp=datetime.utcnow().date().isoformat()
    )

    await db.commit()
    return tariff


async def delete_insurance_rate(db: AsyncSession, id: int):
    delete_tariff = await get_id_rate(db, id)
    if not delete_tariff:
        raise ValueError("Тариф не найден")
    log_event(
        user_id=None,
        action=f"Удаление тарифа ID {id}",
        timestamp=datetime.utcnow().date().isoformat()
    )
    await db.delete(delete_tariff)
    await db.commit()
    return delete_tariff


async def add_insurance_rate(db: AsyncSession, date: datetime, cargo: str, rate: float):
    log_event(
        user_id=None,
        action=f"Добавление тарифа на дату {date.date().isoformat()} для типа груза {cargo} с тарифом {rate}",
        timestamp=datetime.utcnow().date().isoformat()
    )
    new_rate = Tariff(date=date.date(), cargo_type=cargo, rate=rate)
    db.add(new_rate)
    await db.commit()
    return new_rate

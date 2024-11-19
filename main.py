from datetime import datetime
from fastapi import FastAPI
import json
from sqlalchemy.future import select
from app.database.database import db
from app.database.database import async_session
from app.models.models_tariff import Tariff
from app.api.routers import router

app = FastAPI()
app.include_router(router)


async def load_tariffs():
    async with async_session() as session:
        result = await session.execute(select(Tariff))
        tariffs = result.scalars().all()
        if not tariffs:
            with open('tariffs.json') as f:
                data = json.load(f)
                for date_str, tariffs in data.items():
                    # Преобразуем строку даты в объект datetime.date
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

                    for tariff in tariffs:
                        new_tariff = Tariff(cargo_type=tariff['cargo_type'], rate=tariff['rate'], date=date_obj)
                        session.add(new_tariff)
                await session.commit()


@app.on_event("startup")
async def startup():
    await connect()
    await load_tariffs()


async def connect():
    await db.connect()


async def disconnect():
    await db.disconnect()
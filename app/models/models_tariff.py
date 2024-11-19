from sqlalchemy import Column, Integer, String, Float,Date
from app.database.database import Base


class Tariff(Base):
    __tablename__ = "cargo_rates"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, index=True)
    rate = Column(Float, nullable=False)
    date = Column(Date, nullable=False)


from sqlalchemy import Column, Integer, Float, String
from .db import Base


class Anomaly(Base):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(String, index=True)
    value = Column(Float)

    anomaly = Column(Integer)
    zscore_flag = Column(Integer)
    isolation_flag = Column(Integer)
from sqlalchemy.orm import mapped_column, Mapped
from geoalchemy2.types import Point

from database import Database

Base = Database.get_base()


class SurflineSpot(Base):
    __tablename__ = "surfline_spot"

    id: Mapped[int] = mapped_column(primary_key=True)
    spot_id: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[Point] = mapped_column(nullable=False)



class SurflineReport(Base):
    __tablename__ = "surfline_forecast"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[int]
    min: Mapped[int]
    max: Mapped[int]
    plus: Mapped[bool]
    humanRelation: Mapped[str]
    raw: Mapped[str]
    optimalScore: Mapped[int]
    accurateRating: Mapped[bool]
    realMin: Mapped[int]
    realMax: Mapped[int]
    comments: Mapped[str]


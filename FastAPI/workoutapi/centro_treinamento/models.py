from FastAPI.workoutapi.atleta.models import AtletaModel
from workoutapi.contrib.models import BaseModel
from sqlalchemy import Mapped, mapped_column, Integer, String, relationship


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'cenotrs_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
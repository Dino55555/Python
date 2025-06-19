from FastAPI.workoutapi.categorias.models import CategoriaModel
from FastAPI.workoutapi.centro_treinamento.schemas import CentroTreinamento
from workoutapi.contrib.models import BaseModel
from sqlalchemy import ForeignKey, Mapped, mapped_column, Integer, String, Float, DateTime, relationship
from datetime import datetime


class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique = True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_treinamento: Mapped['CentroTreinamento'] = relationship(back_populates='atleta')
    centro_treinamento_id = Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))
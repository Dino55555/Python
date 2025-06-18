from FastAPI.workoutapi.atleta.models import AtletaModel
from workoutapi.contrib.models import BaseModel
from sqlalchemy import ForeignKey, Mapped, mapped_column, Integer, String, relationship

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='atleta')
    categoria_id = Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
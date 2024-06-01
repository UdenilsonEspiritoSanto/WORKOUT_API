from datetime import datetime
import string
from sqlalchemy import DateTime, ForeignKey, Integer
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationship

class AtletaModel(BaseModel):
      __tablename__='atletas'
      pk_id:Mapped[int]=mapped_column(Integer,primary_key=True)
      nome:Mapped[int]=mapped_column(string(50), nullable=False)
      cpf:Mapped[int]=mapped_column(string(11),unique=True, nullable=False)
      idade:Mapped[int]=mapped_column(Integer, nullable=False)
      peso:Mapped[int]=mapped_column(float, nullable=False)
      altura:Mapped[int]=mapped_column(float, nullable=False)
      create_at:Mapped[datetime]=mapped_column (DateTime, nullable=False)
      categoria:Mapped['CategoriaModel']=relationship(back_populates='atleta')
      categoria_id:Mapped[int]=mapped_column(ForeignKey('categorias.pk_id'))
      centro_treinamneto:Mapped['CentroTreinamentoModel']=relationship(back_populates='atleta')
      centro_treinamento_id:Mapped[int]=mapped_column(ForeignKey('centros_treinamento.pk_id'))
import string
from sqlalchemy import Integer
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationship

class CentroTreinamentoModels(BaseModel):
      __tablename__='centros_treinamento'
      pk_id:Mapped[int]=mapped_column(Integer,primary_key=True)
      nome:Mapped[int]=mapped_column(string(30), unique=True,nullable=False)
      endereco:Mapped[int]=mapped_column(string(60), nullable=False)
      proprietario:Mapped[int]=mapped_column(string(20), nullable=False) 
      atleta:Mapped['AtletaModel']=relationship(back_populates='centro_treinamento')
      
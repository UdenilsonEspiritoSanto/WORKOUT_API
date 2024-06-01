import string
from sqlalchemy import Integer
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationship

class CategoriaModel(BaseModel):
      __tablename__='categorias'
      pk_id:Mapped[int]=mapped_column(Integer,primary_key=True)
      nome:Mapped[int]=mapped_column(string(50), unique=True,nullable=False)
      atleta:Mapped['AtletaModel']=relationship(back_populates='categoria')
      
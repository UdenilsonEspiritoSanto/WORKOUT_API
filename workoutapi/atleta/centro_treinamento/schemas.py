from typing import Annotated
from pydantic import BaseModel,Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome:Annotated[str,Field(description='nome do centro de treinamento',example='CT King',max_length=20)]
    endereco:Annotated[str,Field(description='endereco',example='Rua x Quadra 2',max_length=60)]
    nome:Annotated[str,Field(description='nome do centro de treinamento',example='Marcos',max_length=30)]
   
   
   
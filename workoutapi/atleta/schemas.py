from typing import Annotated
from pydantic import BaseModel,Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome:Annotated[str,Field(description='nome do atleta',example='joao',max_length=50)]
    cpf:Annotated[str,Field(description='cpf do atleta',example='12345678912',max_length=11)]
    idade:Annotated[int,Field(description='idade do atleta',example=25)]
    peso:Annotated[PositiveFloat, Field(description='peso do atleta',example=78.5)]
    altura:Annotated[PositiveFloat, Field(description='tamanho do atleta',example=1.78)]
    sexo:Annotated[str, Field(description='sexo do atleta',example='M',max_length=1)]
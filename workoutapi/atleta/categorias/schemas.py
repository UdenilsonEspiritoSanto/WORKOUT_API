
from typing import Annotated
from pydantic import BaseModel, Field


class Categoria(BaseModel):
   nome:Annotated[str,Field(description='nome da categoria',example='Scale',max_length=10)]
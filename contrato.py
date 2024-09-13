from datetime import datetime, date, time
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = 'abacaxi'
    produto2 = 'banana'
    produto3 = 'caqui'
    produto4 = 'damasco'
class Vendas(BaseModel):
    email:EmailStr
    data: date
    hora: time
    produto:ProdutoEnum
    qtt:PositiveFloat
    valor:PositiveInt


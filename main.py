
from fastapi import FastAPI, HTTPException, Response
from ulid import ULID
from pydantic import BaseModel

app = FastAPI()

class Corrida(BaseModel):
    id: str | None = None
    origem: str 
    destino: str
    distancia: int
    valor: float | None = None
    estado: str | None = None

def calculo_valor(distancia:int) -> float:
    tarifa = 6.65
    km = 2.00
    total = tarifa + (km+distancia)
    return total

corridas: list[Corrida] = [
    Corrida(
        id=str(ULID()),
        origem='Centro',
        destino='Dirceu',
        distancia=10,
        valor=calculo_valor(10),
        estado='Requisitada'
        )
]

@app.post('/corridas')
def criar_corrida(corrida: Corrida):
    corrida.id = str(ULID()),
    corrida.valor = calculo_valor(corrida.distancia),
    corrida.estado = 'Requisitada'
    corridas.append(corrida)
    return corrida

@app.delete("/corridas/{id}")
def remove_lista(id:str):
    for c in corridas:
        if c.id == id:
            corridas.remove(c)
            return {"message": "Corrida deletada com sucesso"}
        raise HTTPException(status_code=404,detail='Não localizado.')
    
@app.get('/corridas')
def corridas_lista() -> list[Corrida]:
    return corridas
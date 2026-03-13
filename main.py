from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from bfs2 import busca_solucion_BFS  # Importamos tu función

app = FastAPI(title="BFS Solver API")

# Definimos el formato de entrada
class PuzzleRequest(BaseModel):
    estado_inicial: List[int]
    solucion: List[int]

@app.post("/resolver")
def resolver_puzzle(request: PuzzleRequest):
    # Ejecutamos tu lógica
    nodo_solucion = busca_solucion_BFS(request.estado_inicial, request.solucion)
    
    if nodo_solucion is None:
        raise HTTPException(status_code=404, detail="No se encontró solución")

    # Reconstruimos el camino para enviarlo al Front-end
    camino = []
    nodo_actual = nodo_solucion
    while nodo_actual is not None:
        camino.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    
    camino.reverse()
    return {"pasos": camino, "total_pasos": len(camino) - 1}
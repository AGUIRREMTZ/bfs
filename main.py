from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from bfs2 import busca_solucion_BFS

app = FastAPI(title="BFS Solver API")

# --- CONFIGURACIÓN DE CORS ---
# Esto permite que tu archivo HTML (Front-end) pueda hacer peticiones a tu API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, cambia "*" por la URL de tu front-end si lo despliegas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definimos el formato de entrada
class PuzzleRequest(BaseModel):
    estado_inicial: List[int]
    solucion: List[int]

@app.post("/resolver")
def resolver_puzzle(request: PuzzleRequest):
    # Validamos que los datos tengan 4 elementos como en tu lógica
    if len(request.estado_inicial) != 4 or len(request.solucion) != 4:
        raise HTTPException(status_code=400, detail="Los estados deben tener 4 elementos")
    
    # Ejecutamos la lógica de bfs2.py
    nodo_solucion = busca_solucion_BFS(request.estado_inicial, request.solucion)
    
    if nodo_solucion is None:
        raise HTTPException(status_code=404, detail="No se encontró solución")

    # Reconstruimos el camino
    camino = []
    nodo_actual = nodo_solucion
    while nodo_actual is not None:
        camino.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    
    camino.reverse()
    return {"pasos": camino, "total_pasos": len(camino) - 1}

# Para probar localmente: uvicorn main:app --reload

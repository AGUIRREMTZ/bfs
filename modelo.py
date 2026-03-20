from pydantic import BaseModel
from typing import List, Dict

# Define una conexión entre dos ciudades
class Conexion(BaseModel):
    origen: str
    destino: str
    distancia: float

# Define la solicitud completa que viene del Front-end
class RutaRequest(BaseModel):
    ciudad_inicio: str
    ciudad_destino: str
    conexiones: List[Conexion]  # Toda la red de carreteras
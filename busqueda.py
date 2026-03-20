class Nodo:
    def __init__(self, estado, padre=None, distancia_desde_padre=0, costo_acumulado=0):
        self.estado = estado  # Nombre de la ciudad (ej: "1")
        self.padre = padre
        self.distancia_desde_padre = distancia_desde_padre
        self.costo_acumulado = costo_acumulado

    def get_camino(self):
        # Reconstruye la ruta desde el inicio hasta este nodo
        nodo_actual = self
        camino = []
        while nodo_actual:
            camino.append({
                "ciudad": nodo_actual.estado,
                "distancia_tramo": nodo_actual.distancia_desde_padre,
                "costo_total": nodo_actual.costo_acumulado
            })
            nodo_actual = nodo_actual.padre
        return camino[::-1] # Invierte para que vaya de inicio a fin

def busca_ruta_BFS(inicio, destino, mapa):
    """
    inicio: str (ej: "1")
    destino: str (ej: "6")
    mapa: Dict (ej: {"1": [{"destino": "2", "distancia": 210}], ...})
    """
    nodo_inicial = Nodo(estado=inicio)
    
    # BFS estándar
    frontera = [nodo_inicial]
    visitados = set()

    while frontera:
        nodo_actual = frontera.pop(0) # FIFO
        
        # Si llegamos al destino, devolvemos el camino reconstruido
        if nodo_actual.estado == destino:
            return nodo_actual.get_camino()
        
        if nodo_actual.estado not in visitados:
            visitados.add(nodo_actual.estado)
            
            # Obtener las ciudades vecinas desde el mapa dinámico
            vecinos = mapa.get(nodo_actual.estado, [])
            for vecino in vecinos:
                nueva_ciudad = vecino["destino"]
                distancia = vecino["distancia"]
                
                # Crear nuevo nodo con el costo acumulado
                nuevo_nodo = Nodo(
                    estado=nueva_ciudad,
                    padre=nodo_actual,
                    distancia_desde_padre=distancia,
                    costo_acumulado=nodo_actual.costo_acumulado + distancia
                )
                
                if nueva_ciudad not in visitados:
                    frontera.append(nuevo_nodo)
                    
    return None # No se encontró ruta

# Para probar localmente si el algoritmo funciona con tu imagen
if __name__ == "__main__":
    # Estructura del mapa de la imagen
    mapa_imagen = {
        "1": [{"destino": "2", "distancia": 210}],
        "2": [{"destino": "1", "distancia": 210}, {"destino": "4", "distancia": 201}, {"destino": "5", "distancia": 617}, {"destino": "6", "distancia": 603}, {"destino": "3", "distancia": 355}],
        "3": [{"destino": "2", "distancia": 355}, {"destino": "5", "distancia": 109}, {"destino": "6", "distancia": 346}],
        "4": [{"destino": "2", "distancia": 201}, {"destino": "5", "distancia": 110}],
        "5": [{"destino": "2", "distancia": 617}, {"destino": "4", "distancia": 110}, {"destino": "6", "distancia": 97}, {"destino": "3", "distancia": 109}],
        "6": [{"destino": "2", "distancia": 603}, {"destino": "5", "distancia": 97}, {"destino": "3", "distancia": 346}]
    }
    
    ruta = busca_ruta_BFS("1", "6", mapa_imagen)
    print("Ruta encontrada:", ruta)
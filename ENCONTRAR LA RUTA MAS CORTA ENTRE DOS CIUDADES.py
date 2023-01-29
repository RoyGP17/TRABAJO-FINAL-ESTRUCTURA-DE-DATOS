class Ciudad:
    def __init__(self, nombre, vecinos):
        self.nombre = nombre
        self.vecinos = vecinos

ciudades = {
    'A': Ciudad('A', ['B', 'C']),
    'B': Ciudad('B', ['A', 'D', 'E']),
    'C': Ciudad('C', ['A', 'F']),
    'D': Ciudad('D', ['B']),
    'E': Ciudad('E', ['B', 'F']),
    'F': Ciudad('F', ['C', 'E'])
}

def buscar_ruta(inicio, fin, camino=None):
    if camino is None:
        camino = []
    camino = camino + [inicio]
    if inicio == fin:
        return camino
    if inicio not in ciudades:
        return None
    for ciudad in ciudades[inicio].vecinos:
        if ciudad not in camino:
            nuevo_camino = buscar_ruta(ciudad, fin, camino)
            if nuevo_camino:
                return nuevo_camino
    return None

origen = input("Ingrese el nombre de la ciudad de origen: ")
destino = input("Ingrese el nombre de la ciudad de destino: ")

ruta = buscar_ruta(origen, destino)

if ruta:
    print("La ruta más corta es: ", ruta)
else:
    print("No se encontró una ruta entre las ciudades.")
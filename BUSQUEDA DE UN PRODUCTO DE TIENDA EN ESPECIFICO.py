inventario = {'camisetas': 10, 'pantalones': 5, 'zapatos': 8, 'gorras': 15}

def buscar_producto(producto):
    if producto in inventario:
        return inventario[producto]
    else:
        return 'Producto no encontrado'

producto_buscado = input('Ingrese el nombre del producto que busca:')
print(buscar_producto(producto_buscado))
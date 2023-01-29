print('LISTA DE PACIENTES POR PRIORIDAD EN UN HOSPITAL')
def ordenar_pacientes(pacientes):
    for i in range(len(pacientes)-1):
        for j in range(len(pacientes)-1-i):
            if pacientes[j]['gravedad'] > pacientes[j+1]['gravedad']:
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    return pacientes

pacientes = [{'nombre': 'Juan', 'gravedad': 3}, {'nombre': 'Maria', 'gravedad': 1}, {'nombre': 'Pedro', 'gravedad': 2}]
print(ordenar_pacientes(pacientes))
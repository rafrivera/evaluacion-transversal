planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}
# ITEM 1 ###############################
def leer_opcion():
    try:
        op = int(input(''))
        
        if op > 6 or op < 1:
            raise ValueError
        else:
            return op
    except ValueError:
        print('Debe seleccionar una opción válida')
        return None
########################################

# OP 1 ################################# si es posible agregar deteccion de planes que no existen
def cupos_tipo(tipo):
    planesTipo = []
    
    for i in planes:
        if planes[i][1] == tipo:
            planesTipo.append(i)
            #print(planesTipo)
    
    totalCupos = 0
    
    for j in planesTipo:
        totalCupos += inscripciones[j][1]
        #print(totalCupos)
    
    print(f'Existen {totalCupos} cupos en el plan {tipo}')
########################################

while True:
    print('========== MENÚ PRINCIPAL ==========')
    print('1. Cupos por tipo de plan')
    print('2. Búsqueda de planes por rango de precio')
    print('3. Actualizar precio de plan')
    print('4. Agregar plan')
    print('5. Eliminar plan')
    print('6. Salir')
    print('=====================================')
    
    op = leer_opcion()
    
    if op == None:
        continue
    elif op == 1:
        tipoPlan = input('Escriba el plan a buscar: ').lower()
        cupos_tipo(tipoPlan)
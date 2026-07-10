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
    except ValueError:
        print('Debe seleccionar una opción válida')
        return None
    else:
        return op
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

# OP 2 #################################
def busqueda_precio(p_min, p_max):
    planesRango = []
    
    if p_min <= p_max and p_min >= 0 and p_max >= 0:
        for i in inscripciones:
            if p_min <= inscripciones[i][0] <= p_max:
                planesRango.append(f'{planes[i][0]}--{i}')
                #print(planesRango)
                
        if planesRango != []:
            for j in sorted(planesRango):
                print(j)
        else:
            print('No hay planes en ese rango de precios')
            
    else:
        print('El precio máximo no puede ser menor al precio máximo y ambos tienen que ser mayor o igual que cero')
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
    elif op == 2:
        while True:
            try:
                p_min = int(input('Ingrese el precio mínimo: '))
                p_max = int(input('Ingrese el precio máximo: '))
            except ValueError:
                print('Debe ingresar valores enteros')
                continue
            else:
                busqueda_precio(p_min, p_max)
                break
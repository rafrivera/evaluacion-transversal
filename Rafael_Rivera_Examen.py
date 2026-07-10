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

# OP 1 #################################
def cupos_tipo(tipo):
    if tipo == 'mensual' or tipo == 'trimestral' or tipo == 'anual':
        planesTipo = []
        
        for i in planes:
            if planes[i][1] == tipo:
                planesTipo.append(i)
                #print(planesTipo)
        
        totalCupos = 0
        
        for j in planesTipo:
            totalCupos += inscripciones[j][1]
            #print(totalCupos)
        
        print(f'El total de cupos disponibles es: {totalCupos}')
    else:
        print('Plan no encontrado')
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
            print(f'Los planes encontrados son: {sorted(planesRango)}')
        else:
            print('No hay planes en ese rango de precios')
            
    else:
        print('El precio máximo no puede ser menor al precio máximo y ambos tienen que ser mayor o igual que cero')
########################################

# OP 3 #################################
def buscar_codigo(codigo): # Usada tambien en la opción 5
    if codigo in inscripciones.keys():
        return True
    else:
        return False
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo) == True:
        inscripciones[codigo][0] = nuevo_precio
        return True
    else:
        return False
########################################

# OP 4 #################################
def val_codigo(dato):
    if dato != '' and dato.strip() != '' and dato not in planes.keys():
        return True
    else:
        return False
def val_nombre(dato):
    if dato != '' and dato.strip() != '':
        return True
    else:
        return False
def val_tipo(dato):
    if dato == 'mensual' or dato == 'trimestral' or dato == 'anual':
        return True
    else:
        return False
def val_duracion(dato):
    if dato > 0:
        return True
    else:
        return False
def val_acceso_piscina(dato):
    if dato == 's':
        return True
    else:
        return False
def val_incluye_clases(dato):
    if dato == 's':
        return True
    else:
        return False
def val_horario(dato):
    if dato != '' and dato.strip() != '':
        return True
    else:
        return False
def val_precio(dato):
    if dato > 0:
        return True
    else:
        return False
def val_cupos(dato):
    if dato >= 0:
        return True
    else:
        return False

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    if codigo not in planes:
        planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
        inscripciones[codigo] = [precio, cupos]
        return True
    else:
        return False
########################################

# OP 5 #################################
def eliminar_plan(codigo):
    if buscar_codigo(codigo) == True:
        planes.pop(codigo)
        inscripciones.pop(codigo)
        return True
    else:
        return False
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
    elif op == 3:
        while True:
            try:
                codigo = input('Ingrese el plan a actualizar: ').upper()
                nuevo_precio = int(input('Ingrese el nuevo precio a asignar: '))
                
                if nuevo_precio < 0:
                    raise ValueError
            except ValueError:
                print('Ingrese un precio válido')
                print('-' * 20)
                continue
            else:
                if actualizar_precio(codigo, nuevo_precio) == True:
                    print('Precio actualizado')
                else:
                    print('El código no existe')
                    
                op_otro = input('¿Desea actualizar otro precio (s/n)?: ').lower()
                    
                if op_otro == 's':
                    continue
                else:
                    break
    elif op == 4:
        hay_False = []
        
        add_codigo = input('Ingrese codigo del plan: ').upper()
        hay_False.append(val_codigo(add_codigo))
        
        add_nombre = input('Ingrese nombre del plan: ').capitalize()
        hay_False.append(val_nombre(add_nombre))
        
        add_tipo = input('Ingrese tipo (mensual/trimestral/anual): ').lower()
        hay_False.append(val_tipo(add_tipo))
        
        # add_duracion ################################
        while True:
            try:
                add_duracion = int(input('Ingrese duración (meses): '))
            except ValueError:
                print('Ingrese un número válido')
                continue
            else:
                hay_False.append(val_duracion(add_duracion))
                break
        ###############################################
        add_acceso_piscina = input('¿Incluye acceso a piscina? (s/n): ').lower()
        hay_False.append(val_acceso_piscina(add_acceso_piscina))
        
        add_incluye_clases = input('¿Incluye clases grupales? (s/n): ').lower()
        hay_False.append(val_incluye_clases(add_incluye_clases))
        
        add_horario = input('Ingrese horario: ')
        hay_False.append(val_horario(add_horario))
        
        # add_precio ##################################
        while True:
            try:
                add_precio = int(input('Ingrese precio: '))
            except ValueError:
                print('Ingrese un precio válido')
                continue
            else:
                hay_False.append(val_precio(add_precio))
                break
        ###############################################
        
        # add_cupos ###################################
        while True:
            try:
                add_cupos = int(input('Ingrese cupos: '))
            except ValueError:
                print('Ingrese un número válido')
                continue
            else:
                hay_False.append(val_cupos(add_cupos))
                break
        ###############################################
        
        if False in hay_False:
            print('Error. Registro fallido')
        else:
            agregar_hecho = agregar_plan(add_codigo, add_nombre, add_tipo, add_duracion, add_acceso_piscina, add_incluye_clases, add_horario, add_precio, add_cupos)
            
            if agregar_hecho == True:
                print('Plan agregado')
            else:
                print('El código ya existe')
    elif op == 5:
        planEliminar = input('Ingrese el plan a eliminar: ').upper()
        eliminar_hecho = eliminar_plan(planEliminar)
        
        if eliminar_hecho == True:
            print(planes)
            print('Plan eliminado')
        else:
            print('El código no existe') 
    elif op == 6:
        print('Programa finalizado')
        break
"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Crear el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- REQ. 1: Contar los avistamientos en una ciudad")
    print("4- REQ. 2: Contar los avistamientos por duración")
    print("5. REQ. 3: Contar avistamientos por Hora/Minutos del día")
    print("6. REQ. 4: Contar los avistamientos en un rango de fechas")
    print("7. REQ. 5: Contar los avistamientos de una Zona Geográfica")  
    print("8. REQ. 6 (BONO): Visualizar los avistamientos de una zona geográfica")  
    print("0- Salir")

catalog = None
file = 'UFOS//UFOS-utf8-small.csv'


#funciones de impresión
def printFirst5 (catalog):
    lista = lt.subList(catalog['avistamientos'], 1, 5)
    i = 1
    for avista in lt.iterator(lista):
        print(f"{i}. {avista}\n")
        i +=1

def printLast5 (catalog):
    lista = lt.subList(catalog['avistamientos'], lt.size(catalog['avistamientos'])-4, 5)
    i = 1
    for avista in lt.iterator(lista):
        print(f"{i}. {avista}\n")
        i +=1

def printAvistaCity(avistamientos, city):
    pass

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nCreando el catálogo ....\n")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos ....")
        controller.loadData(catalog, file)
        print("\nAvistamientos cargados: "+ str(lt.size(catalog['avistamientos'])))
        print("\nPrimeros 5 avistamientos: \n")
        printFirst5(catalog)
        print("\nÚltimos 5 avistamientos: \n")
        printLast5(catalog)
        print("")
    
    elif  int(inputs[0]) == 3:
        city = input("\nIngrese el nombre de la ciudad a consultar: ")
        avistamientos = controller.avistaCity(catalog, city)
        #if avistamientos:
        print("\nAltura del árbol: " + str(om.height(catalog['city'])) )
        print("Elementos en el árbol: " + str(om.size(catalog['city'])) +"\n")
        printAvistaCity (avistamientos, city)

        #else:
            #print("\nIngrese una ciudad disponible")

    else:
        sys.exit(0)
sys.exit(0)

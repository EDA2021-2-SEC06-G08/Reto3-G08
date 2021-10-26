"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'avistamientos': None,
                'city': None}
    catalog['avistamientos'] = lt.newList('ARRAY_LIST')
    catalog['city'] = om.newMap('RBT')
    
    return catalog
    

# Funciones para agregar informacion al catalogo

def addAvist(catalog, avist):
    lt.addLast(catalog['avistamientos'], avist)

    if om.contains(catalog['city'], avist['city']):
        lt.addLast(me.getValue(om.get(catalog['city'], avist['city'])), avist)
    else:
        om.put(catalog['city'], avist['city'], lt.newList("ARRAY_LIST"))
        lt.addLast(me.getValue(om.get(catalog['city'], avist['city'])),avist)
    return catalog

# Funciones para creacion de datos

# Funciones de consulta
def avistaCity(catalog, city):
    pass
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

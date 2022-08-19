#S Y S
import sys
print(sys.version)#la version de python utilizado
print()
from getpass import getuser
print(getuser())#nombre del usuario usado del sistema
from subprocess import call
print(call(['ping', 'google.com']))#ejecutar comandos externos, como el ping de
print()
nombre_script= sys.argv[0]
cantidad_arg = len(sys.argv)
argumentos = str(sys.argv)
print()
print('para saber la cantidad de lineas del terminal:')
print('Nombre de script: {}'.format(nombre_script))
print('Cantidad de argumentos: {}'.format(cantidad_arg))
print('Lista de argumentos: {}'.format(argumentos))
#en resumen es cuando en el terminal coloco python (nombre del archivo), ese nombre es el script
#y lo que ponga en adelante con espacios son lineas del terminar adicionales al ejecutar el script
#si no coloco nada me manda la ruta del script
print('\n')
print('Determinar el orden o clasificacion de los bytes de la ejecucion del script')
#mirar si es Little o Big-Endian
print(sys.byteorder)#es como mirar si el codigo esta bien o demora mucho en ejecutar
#modulos que tiene sys
print('\n')
print('los modulos que tanto usamos en sys son:', ', '.join(sys.builtin_module_names))
print('\n')

print('Tamaño de un objeto representable es con sys.getsizeof')
print('el tamaño en Bytes de florencia es:', sys.getsizeof('florecia'), 'Bytes')
print('\n')





#O S
import os
nombre_archivo = 'libreria calendar.py'
print(os.path.isfile(nombre_archivo))#comprobar si existe un archivo en una direccion del pc
print()
import multiprocessing
print(multiprocessing.cpu_count())#nucleos del
print()
print('cuales archivos en esta ruta de librerias y modulos')
RUTA = r'C:\Users\14-baoo1-la\Desktop\Python\python complejo\librerias y modulos'#r es de ruta
from os import listdir#mira todos los archivos que tienen esa (ruta) dentro de su ruta | listdir(ruta)
from os.path import isfile, join#isfile mira si es archivo y no carpeta o algo así | isfile(archivo)
s=0#            ignorar abspath
def archivos_de_ruta(ruta):
    archivos = [a for a in listdir(RUTA) if isfile(join(RUTA, a))]# se puede remplazar ese join por (a)
    global noarchivos
    noarchivos = [a for a in listdir(RUTA) if not isfile(a)] #solo para mirar cuales no son archivos
    return archivos
#a se mete a un ciclo for en donde mira cada ruta de cada archivo que tiene en su ruta a RUTA
#luego retorna a SI a es archivo
#join solo mira si la ruta a tiene dentro la ruta de RUTA | join(sub-ruta, ruta_archivo)
print(archivos_de_ruta(RUTA))
print(f'{len(archivos_de_ruta(RUTA))} archivos')
print(f'{len(noarchivos)} no es archivo, es una carpeta que se llama ({noarchivos[0]})')
print('\n')
import os.path, time
archivo = r'C:\Users\14-baoo1-la\Desktop\Python\python basico\curso 5 y 6\cercania al 1000.py'
print(f'Fecha de creacion: {time.ctime(os.path.getctime(__file__))}')#saber la fecha de creacion del archivo sabiendo si ruta
print(f'Fecha de modificacion: {time.ctime(os.path.getctime(archivo))}')#ultima fecha de modificacion
print(f'Fecha de acceso: {time.ctime(os.path.getatime(archivo))}')
#__file__ es la ruta del archivo actual

#
print('\n')
print('saber todas las rutas de los archivos de una ruta y organizarlos de mas actual fecha de creacion a mas vieja')
import glob
ruta = r'C:\Users\14-baoo1-la\Desktop\Python\python complejo\librerias y modulos'
archivos = glob.glob(ruta + os.path.sep + '*.py')#glob detecta archivos con cierta extencion, os.path.sep es el separador (\) que indica >
#que la ruta se une lo nombres que glob retorna que tengan (*(algo).py)
# los mete en una lista
archivos.sort(key= lambda x: os.path.getctime(x), reverse=True)
print('\n'.join(archivos))
print('\n')
print('imprimir el tamaño de un archivo en Bytes')#con la ruta de este
print('El tamaño de cercania al 1000.py:', os.path.getsize(archivo), 'Bytes')
from sys import getsizeof
print('Tamaño de un objeto representable en Bytes es >', getsizeof(nombre_archivo))
print('\n')
print('saber con os.path.isdir si una ruta es un directorio o is.path.isfile si es un archivo')
ruta = r'C:\Users\14-baoo1-la\Desktop\Python'
from os.path import isdir
def validar_ruta(ruta):
    if os.path.isdir(ruta):
        return 'Es un directorio'
    elif os.path.isfile(ruta):
        return 'Es un archivo'
    else:
        return 'Es un archivo especial'
print(validar_ruta(ruta))
ruta_dos = r'C:\Users\14-baoo1-la\Desktop\Python\python complejo\librerias y modulos\modulos os, time y glob.py'
print(validar_ruta(ruta_dos))
print()
print('nombre de archivo (con su ruta)')
print(os.path.basename(ruta_dos))#saber nombre del archivo en la ruta, para faciliar las cosas

print('')
print('config del sistema operativo con os.environ...')
#print(os.environ) | para saber la configuracion del usuario en si sitema operativo
print('\n')
print('saber la ruta sepadara de la extencion')
print(os.path.splitext(os.path.basename(ruta_dos)))#separa la extencion del nombre o >
print(os.path.splitext(ruta_dos))#separa la extencion de la ruta
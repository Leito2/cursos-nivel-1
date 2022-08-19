# R --> Lectura
# W --> Sobre escritura
# A --> Agregar escritura

def read():
    numbers = []
    with open("../../z_archivos/python/texto_numbers.txt", "r", encoding = 'utf-8') as texto: #leer archivos
        for line in texto:
            numbers.append(int(line))
        print(numbers)

def write():
    names  = ['Facundo', 'Cristian', 'Leandro', 'Leonel', 'Jacobo']
    with open('../../z_archivos/python/texto_names.txt', 'w') as texto:
        for name in names:
            texto.write(name)
            texto.write('\n')
def append():
    names  = ['Maria', 'Pedro']
    with open('../z_archivos/python/texto_names.txt', 'a') as texto: #este agrega texto
        for name in names:
            texto.write(name)
            texto.write('\n')

def run():
    read()
    write()

if __name__ == '__main__':
    run()

#    os.system('cls')
#   sirve para reinicial la terminar de consola y es ejecular ese comando automaticamente

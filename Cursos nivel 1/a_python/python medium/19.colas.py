#C O L A S
#el primero en entrar es el primero en
#solo cambia que usan append() y pop(0)
#en ocaciones hacen esto
#from collections import deque {y quitan elementos con pop.left o algo así} y seria lo mismo que esto
print('colas\n')

cola = ['maria', 'leandro', 'jose', 'mario']
print(cola)

#para agregar se agrega obvio al final

cola.append('carla')
cola.append('flor')
print(cola)
# ['maria', 'leandro', 'jose', 'mario', 'carla', 'flor']

#para quitar es por el inicio

primer_atendido = cola.pop(0)
print(f'en {cola} ya no esta {primer_atendido} ya que la estan atendiendo')
# en ['leandro', 'jose', 'mario', 'carla', 'flor'] ya no esta maria ya que la estan atendiendo
#claro si esto fuera una cola del supermercado
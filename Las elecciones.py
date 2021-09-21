# Las Elecciones
#
#
# El programa debe calcular el ganador de unas elecciones e imprimir su nombre.
# Para este ejemplo se asume que no hay empates
# Los nombres y la cantidad de candidatos es desconocida
#
# Formato de entrada:
# El programa primero recibe un numero N, la cantidad de votos totales que se realizaron.
# Luego recibe N votos en formato cadena, cada uno consiste en el nombre del candidato seleccionado.
#
# Restricciones:
# 1 <= N <= 100
#
# Formato de Salida:
# El programa debe calcular el ganador de las elecciones e imprimir su nombre.


lista = []
lista_candidatos = []
candidatos = {}
mayor = 0
ganador = 0

cantidad = int(input("Numero de votos: "))

for i in range(cantidad):
    voto = input("Cual es tu voto?: ")
    lista.append(voto)
    
for i in range(len(lista)):
    candidato = lista[i]
    if candidato not in lista_candidatos:
        lista_candidatos.append(candidato)
        
for i in range(len(lista_candidatos)):
    buscar = lista_candidatos[i]
    contador = 0
    for k in range(len(lista)):
        if lista[k] == buscar:
            contador += 1
    candidatos[buscar] = contador

for key in candidatos.keys():
    temp = candidatos[key]
    if temp > mayor:
        mayor = candidatos[key]
        ganador = key
        
print("El ganador es:", ganador)


# More code challenges solved in:
# https://github.com/lsfernandez/code_challenges
numeros = input('Digite uma lista de números separada por espaço: ')
lista = numeros.split()

for i in range(len(lista)):
    lista[i] = int(lista[i])
    
media = sum(lista) / len(lista)

print('A média seria:', media)
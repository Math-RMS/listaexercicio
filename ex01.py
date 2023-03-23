numeros = input("Digite uma lista de números separados por espaço: ")

numeros = [int(num) for num in numeros.split()]

pares = []

for num in numeros:
    if num % 2 ==0:
        pares.append(num)

print ("Os números pares da lista são: ", pares)


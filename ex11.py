numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(num) for num in numeros.split()]
impares = []

for num in numeros:
    if num % 2 == 1:
        impares.append(num)

soma = sum(impares)

print ("A soma dos números ímpares da lista são: ", soma)
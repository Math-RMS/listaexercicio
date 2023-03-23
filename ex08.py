numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(num) for num in numeros.split()]
lista = []

for num in numeros:
    if num>10:
        lista.append(num)

print("Os números maiores do que 10 são: ", lista)
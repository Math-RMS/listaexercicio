numeros = input("Digite uma lista de números separados por espaço: ")
numeros = [int(num) for num in numeros.split()]
lista = []

for num in numeros:
    if num<5:
        lista.append(num)
        
print("Os números menores do que 5 são: ", lista)
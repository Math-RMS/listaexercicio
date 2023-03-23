numeros = input('Digite uma lista de números: ')

numeros = [int(num) for num in numeros.split()]

numeros.sort(key=int)

print("A ordem dos números em forma crescente é:", numeros)
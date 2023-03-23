numeros = input('Digite uma lista de números: ')

numeros = [int(num) for num in numeros.split()]

numeros.sort(key=int, reverse=True)

print("A ordem dos números em forma decrescente é:", numeros)
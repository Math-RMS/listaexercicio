numeros = input('Digite alguns números: ')
numeros = [int(num) for num in numeros.split()]

maximo = max(numeros)
minimo = min(numeros)

print('O número maxímo é: ', maximo)
print('O número minimo é: ', minimo)
palavras = str(input("Insira uma lista de palavras: "))

palavras = [str(plr) for plr in palavras.split()]

maior = max(palavras, key=len)
menor = min(palavras, key=len)

print('A maior palvra é: ', maior)
print('A menor palvra é: ', menor)
numeros_duplicados = input("Digite uma lista de números separados por espaço: ")
numeros_duplicados = [int(num) for num in numeros_duplicados.split()]
lista_sem_duplicatas = []

while numeros_duplicados:
    elemento = numeros_duplicados.pop(0) 
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
print("A lista sem duplicatas é:", lista_sem_duplicatas)
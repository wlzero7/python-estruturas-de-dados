# algoritmos/busca_binaria.py

numeros = [10, 20, 30, 40, 50, 60]

inicio = 0
fim = len(numeros) - 1
valor = 40

while inicio <= fim:
    meio = (inicio + fim) // 2

    if numeros[meio] == valor:
        print("Valor encontrado!")
        break

    elif numeros[meio] < valor:
        inicio = meio + 1

    else:
        fim = meio - 1

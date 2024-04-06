def calcular_quadrado_soma_impares(n):
    soma = 0
    impar = 1
    for _ in range(n):
        soma += impar
        impar += 2
    return soma

if __name__ == "__main__":
    try:
        n = int(input("Digite um número natural para calcular o seu quadrado: "))
        if n < 0:
            print("Por favor, digite um número natural.")
        else:
            quadrado = calcular_quadrado_soma_impares(n)
            print(f"O quadrado de {n} é: {quadrado}")
    except ValueError:
        print("Por favor, digite um número natural válido.")

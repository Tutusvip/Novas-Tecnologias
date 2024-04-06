def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

if __name__ == "__main__":
    try:
        n = int(input("Digite um número não negativo para calcular o fatorial: "))
        if n < 0:
            print("Por favor, digite um número não negativo.")
        else:
            resultado = calcular_fatorial(n)
            print(f"O fatorial de {n} é: {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
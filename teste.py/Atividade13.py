def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Digite um número não negativo para calcular o fatorial: "))
        if n < 0:
            print("Por favor, digite um número não negativo.")
        else:
            resultado = calcular_fatorial(n)
            print(f"{n}! = {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
def fibonacci(n):
    if n <= 0:
        return "Por favor, digite um número inteiro positivo maior ou igual a 1."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    try:
        n = int(input("Digite um número inteiro maior ou igual a 3 para encontrar o n-ésimo termo da série de Fibonacci: "))
        resultado = fibonacci(n)
        print(f"O {n}-ésimo termo da série de Fibonacci é: {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

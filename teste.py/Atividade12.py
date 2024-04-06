import math

def verificar_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

def encontrar_primos(n):
    primos_encontrados = []
    numero = 2
    while len(primos_encontrados) < n:
        if verificar_primo(numero):
            primos_encontrados.append(numero)
        numero += 1
    return primos_encontrados

if __name__ == "__main__":
    try:
        n = int(input("Digite a quantidade de números primos que deseja encontrar: "))
        if n <= 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            primos = encontrar_primos(n)
            print(f"Os {n} primeiros números primos são:")
            for primo in primos:
                print(primo, end=" ")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
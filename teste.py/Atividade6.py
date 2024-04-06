import math

def calcular_raizes(a, b, c):
    # Calculando o discriminante
    discriminante = b**2 - 4*a*c

    # Verificando se há raízes reais
    if discriminante < 0:
        print("A equação não possui raízes reais.")
    else:
        # Calculando as raízes
        raiz_discriminante = math.sqrt(discriminante)
        x1 = (-b + raiz_discriminante) / (2*a)
        x2 = (-b - raiz_discriminante) / (2*a)

        # Imprimindo as raízes
        print(f"Raiz x': {x1}")
        print(f"Raiz x'': {x2}")

if __name__ == "__main__":
    try:
        a = float(input("Digite o coeficiente 'a': "))
        b = float(input("Digite o coeficiente 'b': "))
        c = float(input("Digite o coeficiente 'c': "))
        calcular_raizes(a, b, c)
    except ValueError:
        print("Por favor, digite coeficientes válidos (números).")
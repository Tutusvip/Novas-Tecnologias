def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        verificar_par_ou_impar(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

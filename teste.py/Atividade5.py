def separar_digitos(numero):
    # Convertendo o número para uma string para facilitar a iteração
    numero_str = str(numero)

    # Imprimindo os dígitos separados por três espaços
    for digito in numero_str:
        print(digito, end="   ")

if __name__ == "__main__":
    try:
        numero = int(input("Digite um número: "))
        separar_digitos(numero)
    except ValueError:
        print("Por favor, digite um número válido.")
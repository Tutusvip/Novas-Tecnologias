def calcular_digito_verificador(numero_conta):
    # Adiciona os dígitos do número de conta
    soma = sum(int(digito) for digito in numero_conta)
    # Calcula o resto da divisão por 10
    resto_divisao = soma % 10
    # Calcula o dígito verificador
    digito_verificador = 10 - resto_divisao
    # Se o dígito verificador for 10, retorna 0
    if digito_verificador == 10:
        return 0
    else:
        return digito_verificador

if __name__ == "__main__":
    try:
        numero_conta = input("Digite o número da conta (até seis dígitos): ")
        if not numero_conta.isdigit() or len(numero_conta) > 6:
            print("Por favor, digite um número de até seis dígitos.")
        else:
            digito_verificador = calcular_digito_verificador(numero_conta)
            numero_completo = f"00{numero_conta}-{digito_verificador}"
            print(f"Número de conta completo: {numero_completo}")
    except ValueError:
        print("Por favor, digite um número válido.")

def converter_segundos(segundos):
    # Calculando dias, horas, minutos e segundos
    dias = segundos // (24 * 3600)
    segundos %= (24 * 3600)
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    # Imprimindo o resultado
    print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")

if __name__ == "__main__":
    try:
        segundos = int(input("Digite a quantidade de segundos: "))
        if segundos < 0:
            print("Por favor, digite um número positivo.")
        else:
            converter_segundos(segundos)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
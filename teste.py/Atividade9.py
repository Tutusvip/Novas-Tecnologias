def adicao():
    print("\nTabuada de Adição:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} + {j} = {i + j}")

def subtracao():
    print("\nTabuada de Subtração:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} - {j} = {i - j}")

def divisao():
    print("\nTabuada de Divisão:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} / {j} = {i / j}")

def multiplicacao():
    print("\nTabuada de Multiplicação:")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Divisão")
        print("4. Multiplicação")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicao()
        elif opcao == "2":
            subtracao()
        elif opcao == "3":
            divisao()
        elif opcao == "4":
            multiplicacao()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
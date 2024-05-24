def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

# Programa principal
def main():
    while True:
        print(f'\nSelecione a operação:\n')
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')

        escolha = int(input('\nDigite a operação correspondente: '))
        
        if escolha == 5:
            print('Encerrando...')
            break
        elif escolha in (1, 2, 3, 4):
            num1 = int(input('\nDigite o primeiro valor: '))
            num2 = int(input('Digite o segundo valor: '))

            if escolha == 1:
                resultado = somar(num1, num2)
            elif escolha == 2:
                resultado = subtrair(num1, num2)
            elif escolha == 3:
                resultado = multiplicar(num1, num2)
            elif escolha == 4:
                if num2 == 0:
                    print('\nErro! Divisão por 0!')
                    continue
                else:
                    resultado = dividir(num1, num2)

            print(f'\nResultado: {resultado}')
            print('-'*25)
        else:
            print('Opção inexistente!')
if __name__ == "__main__":
    main()
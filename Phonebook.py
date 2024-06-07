from time import sleep

class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, numero):
        if nome in self.contatos:
            print(f'\nContato já existe com o número: {self.contatos[nome]}')
            substituir = input('\nDeseja substituir o número? (s/n): ')
            if substituir == 's':
                self.contatos[nome] = numero
                print('\nNúmero atualizado com sucesso!')
        else:
            self.contatos[nome] = numero
            print('\nContato adicionado com sucesso!')

    def excluir_contato(self, nome):
        if nome not in self.contatos:
            print('Contato inexistente.')
        else:            
            del self.contatos[nome]
            print('Contato removido.')

    def buscar_contato(self, nome):
        if nome not in self.contatos:
            return print('\nContato não encontrado')
        else:
            return self.contatos.get(nome)
    
    def listar_contatos(self):
        if len(self.contatos) == 0:
            print('Lista de Contatos Vazia!')
        else:
            for nome, numero in self.contatos.items():
                print(f'{nome:<10} ---- {numero:<15}')


def limpar_tela():
    import os
    os.system('cls')

def encerrar():
    print('\nEncerrando...')
    sleep(2)
    limpar_tela()
    print('Aplicativo encerrado.')

def retornar():
    print('-'*25)
    input('[Enter] para retornar ')


def menu():    
    agenda = AgendaTelefonica()

    while True:
        limpar_tela()

        print('-'*22)
        print('  Agenda Telefônica')
        print('-'*22)
        print('[ 1 ] Adicionar')
        print('[ 2 ] Buscar')
        print('[ 3 ] Listar')
        print('[ 4 ] Excluir')
        print('[ 5 ] Sair')

        select = str(input('\nSelecione a operação desejada: '))

        match select:
            case '1':
                limpar_tela()

                print('- Adicionar contato -\n')

                nome = str(input('Nome: '))
                telefone = str(input('\nNúmero: '))

                agenda.adicionar_contato(nome, telefone)
                
                retornar()
            case '2':
                limpar_tela()

                print('- Buscar Contato -\n')

                nome = str(input('Qual contato deseja buscar? '))

                numero = agenda.buscar_contato(nome)
                
                if numero:
                    print(f'\nNome: {nome} | Número: {numero}')

                retornar()
            case '3':
                limpar_tela()
                print('- Lista de Contatos -\n')
                agenda.listar_contatos()
                retornar()
            case '4':
                limpar_tela()

                print('- Excluir Contato -\n')

                nome = str(input('Contato que deseja excluir: '))

                print('')
                agenda.excluir_contato(nome)
                retornar()
            case '5':
                encerrar()
                break
            case _:
                print('\nSeleção inválida! Por favor, digite um número de 1 a 5.')

                sleep(2)
        
if __name__ == '__main__':
    menu()

def escolher_palavra():
    import random 

    lista_palavras = ['desenvolvimento', 'python', 'tecnologia', 'programação', 'inovação', 'tendências']

    palavra_aleatoria = random.choice(lista_palavras)

    return palavra_aleatoria

def exibir_forca(tentativas):
    print(f'Chances restantes: ({tentativas}/6)!\n')

def desenha_boneco(erros):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
         =========
        """
    ]
    print(estagios[erros])

def jogar():
    import os
    os.system('cls')

    select = escolher_palavra()
    hide = ["_" for _ in select]
    miss = []
    chances = 6

    print('Bem-vindo ao Hangman!')
    print('-'*30)

    while True:
        guess = input('Tente adivinhar uma Letra: ').lower()
        
        if guess in select:
            for i, letra in enumerate(select):
                if letra == guess:
                    hide[i] = letra
        else:
            miss.append(guess)
            chances -= 1
            desenha_boneco(6 - chances)

        print(f'\nPalavra: {" ".join(hide)}')
        print('-'*30)
        print(f'Letras erradas: {" ".join(miss)}')
        exibir_forca(chances)

        if chances == 0:
            print('Acabaram as tentativas!')
            print(f'Você Perdeu! A palavra era "{select}"')
            break  

        if "".join(hide) == select:
            print('Parabéns! Você venceu!')
            break

if __name__ == "__main__":
    jogar()

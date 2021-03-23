# Treinamento de Python iniciante;
# Um jogo de Forca.
import escolha_seu_jogo as menu

import random


def jogar():
    #  Começo do Código:
    mostrar_boas_vindas()

    palavras = palavra_secreta_aleatoria()

    palavras = random.choice(palavras)

    palavra_secreta = palavras.upper().strip()
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(f'Palavra: {letras_acertadas}')

    enforcou = False
    acertou = False

    erros = 0
    acertos = 0

    while not enforcou and not acertou and '_' in letras_acertadas:

        chute_do_jogador = letra_do_jogador()

        if '_' not in letras_acertadas:  # Serve para identificar que o jogador;
            # completou a palavra, já que não resta mais'_'.
            print('Parabéns, você acertou a palavra.')

        print('=-=' * 15)

        index = 0

        for letra in palavra_secreta:
            if chute_do_jogador in letra:
                acertos += 1
                letras_acertadas[index] = letra
                print(f'Parabéns a letra {chute_do_jogador} '
                      f'estava na palavra.\n{letras_acertadas}')
            index += 1
        if chute_do_jogador not in palavra_secreta:
            erros += 1
            print(f'A palavra não contem'
                  f' essa letra.')
            desenha_forca(erros)

        if erros == 7:
            enforcou = erros
            caveira_desenho()

            print('=-=' * 15)
            print(f'Que pena, a a palavra era: {palavra_secreta}!')
            fazer = int(
                input(f'ENFORCADO, você errou {erros} vezes. Fim de jogo.\n'
                      '[1] Para jogar novamente.\n'
                      '[2] Para sair.'))

            if fazer == 1:
                menu.escolhe_jogo()
            if fazer == 2:
                exit()

            print('=-=' * 15)

        if "_" not in letras_acertadas:
            trofeu()
            fazer = int(input('Parabéns, você acertou a palavra!\n'
                              ' o que quer fazer agora?'
                              '\n[1] Para jogar novamente.'
                              '\n[2] Para sair'))
            print('=-=' * 15)

            if fazer == 1:
                menu.escolhe_jogo()
            if fazer == 2:
                exit()

    print('=-=' * 15)

# Fim do código, tirando As defs.
def mostrar_boas_vindas():
    print('=-=' * 10)
    print('Bem vindo ao jogo da Forca!')
    print('=-=' * 10)


def palavra_secreta_aleatoria():
    palavras = []

    with open('forca_palavras.txt', 'r') as texto:
        for linha in texto:
            linha = linha.strip()
            palavras.append(linha)
    return palavras


def letra_do_jogador():
    chute_do_jogador = str(
        input('Qual letra você acha que'
              ' a palavra contêm?').replace(' ', '').upper())
    return chute_do_jogador


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def trofeu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def caveira_desenho():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# Essa linha de código facilita a execução do código através de outros códigos.
if __name__ == '__main__':
    jogar()

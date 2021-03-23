# Treinamento de Python iniciante;
# Código simples em que o computador gera um número aleatório;
# Jogador tem que acertar o número com finita quantidade de tentativas;
# Jogador ganha pontos baseados na dificuldade escolhida e tentativas de acerto.

from random import randrange
from time import sleep

import escolha_seu_jogo as menu


def jogar():
    #  Começo do Código:
    #  Valores para funcionamento do Código:
    tentativa_do_jogador = 'x'
    chances_restantes: int = 4
    total_de_chutes: int = 0
    # Número aleatório entre 1 e 100.
    numero_aleatorio: int = randrange(1, 101)
    pontos: int = 0

    print('=-=' * 20)
    print('Adivinhe o número que o computador pensou de 1-100!')
    print('=-=' * 20)

    print('Defina a dificuldade do jogo!\n[1] FÁCIL\n[2] NORMAL\n[3] DIFÍCIL')

    dificuldade = int(input('Digite o número da dificuldade:').replace(' ', ''))
    print('=-=' * 20)
    if dificuldade == 1:
        chances_restantes = 10
    if dificuldade == 2:
        chances_restantes = 7
    if dificuldade == 3:
        chances_restantes = 4

    print(f'Você tem {chances_restantes} tentativas!')
    sleep(1)
    print('Processando...')
    sleep(2)

    while tentativa_do_jogador != numero_aleatorio and chances_restantes != 0:

        total_de_chutes += 1
        chances_restantes -= 1
        print('=-=' * 20)

        tentativa_do_jogador = int(input('Qual número, entre 1 e 100,'
                                         ' você acha que ele pensou?:').replace(
            ' ', ''))
        print('=-=' * 20)
        # Nesse .replace Estou tirando possíveis espaços feitos pelo jogador.

        if tentativa_do_jogador < 1 or tentativa_do_jogador > 100:
            print('\n!!ATENÇÃO!! Você tem que digitar um número entre 1 e 100,'
                  ' Não desperdice suas tentativas.')
            print(f'\nVocê tem {chances_restantes} tentativas!')
            continue

        if tentativa_do_jogador == numero_aleatorio:
            pontos += 1 + (chances_restantes + 1) * dificuldade
            print(
                f'Parabéns, o número realmente era o {numero_aleatorio},'
                f' Você precisou de {total_de_chutes} tentativas para acertar.')

            print(
                f'Você já obteve >{pontos}< Pontos.\nContinue Jogando para'
                f' aumentar sua pontuação.\nSe perder,'
                f' sua pontuação será zerada!')
            print('=-=' * 20)

            escolha = int(input(
                '\nDigite [1] para Jogar novamente\nDigite [2] para mudar'
                ' a dificuldade\nDigite [3] para escolher outro jogo\n'
                'Digite [4] para sair.').replace(
                ' ', ''))
            print('=-=' * 20)
            if escolha == 1 and dificuldade == 1:
                chances_restantes = 10
                total_de_chutes -= total_de_chutes
                numero_aleatorio = randrange(1, 101)

            if escolha == 1 and dificuldade == 2:
                chances_restantes = 7
                total_de_chutes -= total_de_chutes
                numero_aleatorio = randrange(1, 101)

            if escolha == 1 and dificuldade == 3:
                chances_restantes = 4
                total_de_chutes -= total_de_chutes
                numero_aleatorio = randrange(1, 101)

            if escolha == 2:
                numero_aleatorio = randrange(1, 101)
                print('\nDefina a dificuldade do jogo!\n[1] FÁCIL\n'
                      '[2] NORMAL\n[3] DIFÍCIL')

                dificuldade = int(input('Digite o número '
                                        'da dificuldade:').replace(' ', ''))
                print('=-=' * 20)

                total_de_chutes -= total_de_chutes

                if dificuldade == 1:
                    chances_restantes = 10
                if dificuldade == 2:
                    chances_restantes = 7
                if dificuldade == 3:
                    chances_restantes = 5

            if escolha == 4:
                print('Obrigado por jogar! Volte Sempre!')
                break
            if escolha == 3:
                menu.escolhe_jogo()
            # Resetando o valor para que não ocorra possível erro.
            tentativa_do_jogador = 'x'

        elif tentativa_do_jogador > numero_aleatorio and chances_restantes != 0:
            print(f'O número não é {tentativa_do_jogador}. Tente um'
                  f' valor Menor!'
                  f' Você ainda tem {chances_restantes} tentativas.')

        elif tentativa_do_jogador < numero_aleatorio and chances_restantes != 0:
            print(
                f'O número não é {tentativa_do_jogador}. Tente um valor Maior!'
                f' Você ainda tem {chances_restantes} Tentativas.')

        escolha = 'x'
        if chances_restantes == 0 and tentativa_do_jogador != numero_aleatorio:
            print(
                f'\nVocê Errou!!! suas tentativas acabaram.\nO número'
                f' escolhido era o {numero_aleatorio}!\nVocê terminou com'
                f' {pontos} pontos! Mais sorte na proxima!')

            pontos -= pontos
            escolha = int(input(
                '\n\nDigite [1] para Jogar novamente\n'
                'Digite [2] Para mudar a dificuldade\n'
                'Digite [3] para escolher outro jogo\n'
                'Digite [4] para sair.').replace(
                ' ', ''))

        if escolha == 1 and dificuldade == 1:
            chances_restantes = 10
            total_de_chutes -= total_de_chutes
            numero_aleatorio = randrange(1, 101)
        if escolha == 1 and dificuldade == 2:
            chances_restantes = 7
            total_de_chutes -= total_de_chutes
            numero_aleatorio = randrange(1, 101)
        if escolha == 1 and dificuldade == 3:
            chances_restantes = 4
            total_de_chutes -= total_de_chutes
            numero_aleatorio = randrange(1, 101)

        if escolha == 2:
            print('Defina a dificuldade do jogo!\n'
                  '[1] FÁCIL\n[2] NORMAL\n[3] DIFÍCIL')
            dificuldade = int(input('Digite o'
                                    ' número da dificuldade:').replace(' ', ''))
            total_de_chutes -= total_de_chutes
            if dificuldade == 1:
                chances_restantes = 10
            if dificuldade == 2:
                chances_restantes = 7
            if dificuldade == 3:
                chances_restantes = 5

            continue
        if escolha == 4:
            print('Obrigado por jogar! Volte Sempre!')
            break
        if escolha == 3:
            menu.escolhe_jogo()
        # Fim do Código - Fim do Código - Fim do Código - Fim do Código!
    print('=-=' * 20)


# Essa linha de código facilita a execução do código através de outros códigos.
if __name__ == '__main__':
    jogar()

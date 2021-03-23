# Treinamento para codificação de Python iniciante.
# Menu para escolher o jogo.

# Importação dos jogos:
import Adivinhe_Computador as Adivinhe
import Forca


def escolhe_jogo():
    print('Escolha o jogo!\n[1] Para Adinhação.\n[2] Para Forca.\n'
          '[3] Para Sair do jogo.')

    jogo = int(input('Digite o número do jogo'
                     ' no qual você deseja jogar:').replace(' ', ''))

    if jogo == 1:
        Adivinhe.jogar() and print('Você escolheu o jogo de Adivinhar.')
    elif jogo == 2:
        Forca.jogar() and print('Você escolheu o jogo da Forca.')
    elif jogo == 3:
        exit()


if __name__ == '__main__':
    escolhe_jogo()

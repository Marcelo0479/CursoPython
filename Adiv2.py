import random

def jogar():

    print('Bem vindo ao jogo de advinhação')

    numero_secreto = random.randrange(1,101)

# Retirei a criação da variável de tentativas antes da atribuição do nível.
# A própria criação do nível já cria a variável, portanto não a necessidade de criá-la antes.

    print("Defina a dificuldadde")
    nivel = int(input("Digite 1 para fácil, 2 para médio, ou 3 para difícil: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    rodada = 1
    pontos = 1000

    for rodada in range(1, tentativas + 1 ):
        print('Tentativa', rodada, 'de', tentativas)

#Usei a função try para que o código não quebre caso seja digitado algum valor inválido.

        try:
            chute = int(input("Digite seu chute: "))

            if (chute < 1 or chute > 100):
                print('Vc deve digitar um número inteiro entre 1 e 100')
                continue

            acertou = numero_secreto == chute
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print('Parabens, vc acertou')
                print('Vc fez {} pontos'.format(pontos))
                break

# Criei um elif aqui para que eu pudesse passar a mensagem que o jogardor perdeu.

            elif (rodada < tentativas):
                if (maior):

# Não criei a variável pontos perditos, pois ela não é necessária.
# Criei uma print da pontuação atual apos cada chute.
# Além disso, mpdifiquei a formula de calculo de perda de pontos, pois com a informação da pontuação parcial
# o jogador poderia fazer a conta e descobrir o número secreto

                    pontos = pontos - (10 * nivel)
                    print('Vc errou. Seu chute foi maior que o número secreto.')
                    print('Vc ainda tem {} pontos. Tente novamente'.format(pontos))
                elif (menor):
                    pontos = pontos - (10 * nivel)
                    print('Vc errou. Seu chute foi menor que o número secreto.')
                    print('Vc ainda tem {} pontos. Tente novamente'.format(pontos))

            else:
                pontos = pontos - (10 * nivel)
                print('Vc perdeu')
                print('Vc fez {} pontos'.format(pontos))

        except ValueError:
            pontos = pontos - (10 * nivel)
            print("O chute digitado não é válido. Digite um número inteiro entre 1 e 100.")
            print('Vc ainda tem {} pontos. Tente novamente'.format(pontos))

        rodada += 1

    print('Fim do jogo')

if (__name__ == "__main__"):
    jogar()

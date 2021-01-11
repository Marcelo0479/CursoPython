import random

def jogar():
    print("Jogo de adivinhação 2")

    numero_secreto = random.randrange(1,100)

    print("Defina a dificuldadde")
    dificuldade = int(input("Digite 1 para fácil, 2 para médio, ou 3 para difícil: "))
    if (dificuldade == 1):
        tentativas = 20
    elif (dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 5

    total_de_tentativas = tentativas
    rodada = 1
    pontos = 1000

    while (tentativas > 0):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        rodada += 1
        tentativas += 1

        try:
            chute = int(input("Digite seu chute de 1 a 100: "))

            if (chute < 1 or chute > 100):
                pontos = pontos - 100 * dificuldade
                print("Você deve digitar um número entre 1 e 100. Você ainda temn {} pontos".format(pontos))
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto

            if (acertou):
                print("Acertou. Você fez {} pontos".format(pontos))
                tentativas = 0
                break
            elif (tentativas != 0):
                if (maior):
                    pontos = pontos - abs(numero_secreto - chute) * dificuldade
                    print(
                        "Errou! Seu chute foi maior que o número secreto. Você ainda tem {} pontos. Tente novamente".format(
                            pontos))
                else:
                    pontos = pontos - abs(numero_secreto - chute) * dificuldade
                    print(
                        "Errou! Seu chute foi menor que o número secreto. Você ainda tem {} pontos. Tente novamente".format(
                            pontos))

            else:
                pontos = pontos - abs(numero_secreto - chute) * dificuldade
                print("Perdeu. Você fez {} pontos.".format(pontos))

        except ValueError:
            pontos = pontos - 150 * dificuldade
            print("Chute digitad não é valido. Você ainda tem {} pontos".format(pontos))
            print("Digite um número entre 1 e 100.")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()

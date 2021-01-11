import random

def jogar():
    print("Jogo de adivinhação")

    Numero_Secreto = random.randrange(1,101)
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Nível de dificuldade")
    dificuldade = int(input("Digite 1 para fácil, ou 2 para médio, ou 3 para difícil: "))

    if(dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        Chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", Chute_str)
        chute = int(Chute_str)

        if(chute < 1 or chute > 100):
            print("Número invalido, Digite um número entre 1 e 100")
            continue

        Acertou = Numero_Secreto == chute
        maior   = Numero_Secreto < chute
        menor   = Numero_Secreto > chute

        if(Acertou):
            print("Acertou")
            print("Pontuação final: {}".format(pontos * dificuldade))
            break
        else:
            if(maior):
                print("Errou, chute maior que o número secreto")
                if(rodada == tentativas):
                    print("O número secreto era {} Você fez {} pontos".format(Numero_Secreto, pontos))
            elif(menor):
                print("Errou, chute menor que o número secreto")
                if (rodada == tentativas):
                    print("O número secreto era {} Você fez {} pontos".format(Numero_Secreto, round(pontos / 10)))
            pontos_perdidos = abs(chute - Numero_Secreto)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo")


if(__name__ == "__main__"):
    jogar()
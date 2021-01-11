import Forca2
import Adiv2

print("Escolha seu jogo")

print("(1) forca, (2) advinhação")

jogo = int(input("Qual o jogo? "))

if(jogo == 1):
    print("Jogando forca")
    Forca2.jogar()
elif(jogo == 2):
    print("Jogando advinhação")
    Adiv2.jogar()


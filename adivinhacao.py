import random
def jogar():
    print("Bem vindo ao jogo de adivinhação!")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1, 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número de 1 a 100: "))
        print("Você digitou: ", chute)
        if chute < 1 or chute > 100:
            print('VocÊ deve digitar um número entr 1 e 100!')
            continue
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos:7.2f}")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto!")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute) / 3
            pontos = pontos - pontos_perdidos
    print(f"O numero secreto era {numero_secreto}. Você fez {pontos} pontos!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
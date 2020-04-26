import random

# Compressão de lista
# inteiros = [1,3,4,5,7,8,9]
# pares = [par for par in inteiros if par % 2 == 0]
# print(pares)

def imprime_mensagem_abertura():
    print('**********************************')
    print('Bem vindo ao jogo da Forca')
    print('**********************************')

def carrega_palavra_secreta():
    # with já fecha o arquivo se acontecer um erro ou nao.
    with open('palavras.txt', 'r') as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    return palavras[random.randrange(0, len(palavras))]

def inicializa_letras_acertadas(palavra_secreta):
    return  ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual a letra? ")
    return chute.strip()

def marcar_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1
    print(letras_acertadas)

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       _____      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
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
    print("       \_     _/         ")
    print("         \___/           ")

def desenha_forca(erros):
    print("  ___     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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
    print("|__         ")
    print()

def jogar():
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    imprime_mensagem_abertura()

    erros = 0
    while(True):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marcar_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print(letras_acertadas)
        if(erros == 7): break

        if("_" not in letras_acertadas): break

    if("_" not in letras_acertadas):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
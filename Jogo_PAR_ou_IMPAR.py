from random import randint
from time import sleep
def par_ou_impar():
    vitorias = 0

    print("Bem-vindo ao jogo Par ou Ímpar!")
    
    while True:
        jogador = int(input("Diga um valor: "))
        computador = randint(0, 10)
        soma = jogador + computador
        resultado = " "
        
        while resultado not in "PI":
            resultado = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]

        print(f"Você digitou {jogador} e o computador {computador}. A soma é \033[32m{soma}\033[m", end=" ")
        print("\033[4mDEU PAR!\033[m" if soma % 2 == 0 else "\033[4mDEU ÍMPAR!\033[m")

        if resultado == "P":
            if soma % 2 == 0:
                sleep(1.3)
                print("\033[36mVocê venceu!\033[m")
                vitorias += 1
            else:
                sleep(1.5)
                print("\033[33mVocê perdeu!\033[m")
                break

        elif resultado == "I":
            if soma % 2 == 1:
                sleep(1.3)
                print("\033[36mVocê venceu!\033[m")
                vitorias += 1
            else:
                sleep(1.3)
                print("\033[33mVocê perdeu!\033[m")
                break

        # Pergunta se o jogador quer continuar
        continuar = input("Você quer continuar jogando? [S/N]: ").strip().upper()
        if continuar != 'S':
            break

    print(f"\033[4;31mGAME OVER!\033[m      Você venceu:  {vitorias} vez(es).")

par_ou_impar()

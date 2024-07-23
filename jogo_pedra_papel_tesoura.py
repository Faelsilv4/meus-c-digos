import random

def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    vitorias_jogador = 0
    vitorias_computador = 0

    print("Bem-vindo ao jogo Pedra, Papel, Tesoura!")
    print("Digite 'sair' para encerrar o jogo.")

    while True:
        escolha_jogador = input("Escolha 'pedra', 'papel' ou 'tesoura': ").lower()

        if escolha_jogador == 'sair':
            break

        if escolha_jogador not in opcoes:
            print("Escolha inválida! Tente novamente.")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"O computador escolheu: {escolha_computador}")

        if escolha_jogador == escolha_computador:
            print("Empate!")
        elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
             (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
             (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
            print("Você venceu!")
            vitorias_jogador += 1
        else:
            print("Você perdeu!")
            vitorias_computador += 1

        print(f"Placar: Jogador {vitorias_jogador} - {vitorias_computador} Computador\n")

    print("Obrigado por jogar!")

pedra_papel_tesoura()

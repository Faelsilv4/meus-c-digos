tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def mostra_tabuleiro():
    print("\n JOGO DA VELHA\n")
    for r, linha in enumerate(tabuleiro):
        print(f'{r + 1} {" | ".join(linha): >11}')
        if r < 2:
            print(f'   {"--" * 6: >11}')

    print(f'{"   1    2    3":>11} \n')


j1 = 1


def jogadas(x, y):
    global j1
    if j1 == 1:
        if tabuleiro[x - 1][y - 1] == " ":
            tabuleiro[x - 1][y - 1] = "X"
            j1 = 2

        else:
            print("ERRO! casa indisponivel.")
            erro()
    else:
        if tabuleiro[x - 1][y - 1] == " ":
            tabuleiro[x - 1][y - 1] = "O"
            j1 = 1

        else:
            print("ERRO! casa indisponivel.")
            erro()


def erro():
    global l, c

    while True:
        l = int(input('linha >> '))
        c = int(input('coluna >> '))
        if 0 < l <= 3 and 0 < c <= 3:
            jogadas(l, c)
            break
        print("erro de localização!")


def ganhador():
    global vencedor, lista_linha
    #linha
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " ":
            vencedor = True
    #coluna
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " ":
            vencedor = True
    #diagonal principal
    if tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        vencedor = True
    #diagonal secundaria
    if tabuleiro[0][2] != " " and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
        vencedor = True
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return "Empate"


vencedor = False

while True:
    mostra_tabuleiro()
    print(f"\njogador {j1}")
    erro()
    ganhador()
    #print(lista_linha)
    if vencedor:
        mostra_tabuleiro()
        print('vencedor X' if j1 == 2 else "vencedor O")
        break

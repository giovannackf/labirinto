
energia = 50
posicao_personagem_x = 0
posicao_personagem_y = 0

def faz_mapa():
        ## faz as paredes da borda
        w, h = 60, 30
        Matrix = [[' ' for x in range(w)] for y in range(h)]
        for i in range(0, 30):
                Matrix[i][0] = '#'
                Matrix[i][59] = '#'

        for j in range(0, 60):
                Matrix[0][j] = '#'
                Matrix[29][j] = '#'
        ### faz as entradas
        Matrix[6][0] = ' '
        Matrix[21][59] = ' '

        ## faz paredes do labirinto
        # linha 4
        for x in range(2, 12):
                Matrix[3][x] = '#'
        # linha 5
        Matrix[4][2] = '#'
        Matrix[4][11] = '#'
        # linha 6
        Matrix[5][1] = '#'
        Matrix[5][2] = '#'
        Matrix[5][11] = '#'
        #linha 7
        Matrix[6][11] = '#'
        #linha 8
        Matrix[7][1] = '#'
        Matrix[7][2] = '#'
        Matrix[7][11] = '#'
        # linha 9
        for x in range(2, 10):
                Matrix[8][x] = '#'
        Matrix[8][11] = '#'
        # linha 10
        Matrix[9][9] = '#'
        Matrix[9][11] = '#'
        # linha 11
        Matrix[10][9] = '#'
        Matrix[10][11] = '#'
        for x in range(32, 46):
                Matrix[10][x] = '#'
        #linha 12
        Matrix[11][9] = '#'
        for x in range(11, 24):
                Matrix[11][x] = '#'
        Matrix[11][32] = '#'
        Matrix[11][45] = '#'
        #linha 13
        Matrix[12][9] = '#'
        Matrix[12][23] = '#'
        Matrix[12][32] = '#'
        Matrix[12][45] = '#'
        #linha 14
        Matrix[13][9] = '#'
        Matrix[13][23] = '#'
        Matrix[13][32] = '#'
        Matrix[13][45] = '#'
        #linha 15
        Matrix[14][9] = '#'
        Matrix[14][23] = '#'
        Matrix[14][32] = '#'
        Matrix[14][45] = '#'
        #linha 16
        Matrix[15][9] = '#'
        Matrix[15][23] = '#'
        Matrix[15][32] = '#'
        for x in range(34, 44):
                Matrix[15][x] = '#'
        Matrix[15][45] = '#'
        for x in range(51, 59):
                Matrix[15][x] = '#'
        #linha 17
        for x in range(9, 14):
                Matrix[16][x] = '#'
        for x in range(15, 24):
                Matrix[16][x] = '#'
        Matrix[16][32] = '#'
        Matrix[16][34] = '#'
        Matrix[16][43] = '#'
        Matrix[16][45] = '#'
        Matrix[16][51] = '#'
        Matrix[16][58] = '#'
        #linha 18
        Matrix[17][13] = '#'
        Matrix[17][15] = '#'
        Matrix[17][32] = '#'
        Matrix[17][34] = '#'
        Matrix[17][43] = '#'
        Matrix[17][45] = '#'
        Matrix[17][51] = '#'
        for x in range(53, 57):
                Matrix[17][x] = '#'
        Matrix[17][58] = '#'
        # linha 19
        Matrix[18][13] = '#'
        Matrix[18][15] = '#'
        for x in range(23, 33):
                Matrix[18][x] = '#'
        for x in range(34, 37):
                Matrix[18][x] = '#'
        for x in range(40, 44):
                Matrix[18][x] = '#'
        for x in range(45, 52):
                Matrix[18][x] = '#'
        Matrix[18][53] = '#'
        Matrix[18][56] = '#'
        Matrix[18][58] = '#'
        # linha 20
        Matrix[19][13] = '#'
        for x in range(15, 24):
                Matrix[19][x] = '#'
        Matrix[19][36] = '#'
        Matrix[19][40] = '#'
        Matrix[19][53] = '#'
        Matrix[19][56] = '#'
        Matrix[19][58] = '#'
        #linha 21
        Matrix[20][13] = '#'
        Matrix[20][36] = '#'
        Matrix[20][40] = '#'
        Matrix[20][53] = '#'
        Matrix[20][56] = '#'
        Matrix[20][58] = '#'
        #linha 22
        for x in range(13, 24):
                Matrix[21][x] = '#'
        Matrix[21][36] = '#'
        Matrix[21][40] = '#'
        Matrix[21][53] = '#'
        Matrix[21][56] = '#'
        #linha 23
        Matrix[22][23] = '#'
        Matrix[22][36] = '#'
        Matrix[22][40] = '#'
        Matrix[22][53] = '#'
        for x in range(56,59):
                Matrix[22][x] = '#'
        #linha 24
        for x in range(23, 37):
                Matrix[23][x] = '#'
        for x in range(40, 54):
                Matrix[23][x] = '#'
        return Matrix



def mostra_mapa(Matrix):
####################################  mostra
        for i in range(0, 30):
                mylist = Matrix[i]
                print('[%s]' % ''.join(map(str, mylist)))
        print(posicao_personagem_x, posicao_personagem_y)
        print(f'Voce possui {energia} pontos de energia')


def cria_personagem(Matrix):
        Matrix[6][0] = '@'
        posicao_personagem_x = 0
        posicao_personagem_y = 6
        return Matrix

def mexer_personagem(Matrix, movimento):
    global energia
    global posicao_personagem_x
    global posicao_personagem_y
    erro = 0
    if movimento == 'w':
            if Matrix[posicao_personagem_y - 1][posicao_personagem_x] != '#':
                Matrix[posicao_personagem_y][posicao_personagem_x] = ' '
                posicao_personagem_y = posicao_personagem_y -1

            else:
                erro =1
    elif movimento == 's':
            if Matrix[posicao_personagem_y + 1][posicao_personagem_x] != '#':
                Matrix[posicao_personagem_y][posicao_personagem_x] = ' '
                posicao_personagem_y = posicao_personagem_y +1

            else:
                erro = 1
    elif movimento == 'd':
            if Matrix[posicao_personagem_y] [posicao_personagem_x+1] != '#':
                Matrix[posicao_personagem_y][posicao_personagem_x] = ' '
                posicao_personagem_x = posicao_personagem_x +1

            else:
                erro = 1
    elif movimento == 'a':
            if Matrix[posicao_personagem_y][posicao_personagem_x -1] != '#':
                Matrix[posicao_personagem_y][posicao_personagem_x] = ' '
                posicao_personagem_x = posicao_personagem_x -1

            else:
                erro = 1
    print(erro)
    if erro != 1:
        Matrix[posicao_personagem_y][posicao_personagem_x] = '@'
        energia = energia-1

def menu():
        print('''bem vindo ao jogo
        [1] comecar a jogar
        [2]sair''')
        escolha = input()
        return escolha
def menu_cont():
        print(''' jogo pausado
        [1]continuar no jogo
        [2]fechar o jogo''')
        escolha = input()
        return escolha
def jogo_principal():
    global escolha
    fim_de_jogo = 0
    while(fim_de_jogo == 0):
        mostra_mapa(mapinha)
        print('escolha o lado que seu personagem deseja andar: ' )
        movimento = input()
        if movimento == 'm':
                 escolha = menu_cont()
        if escolha != '2':
                mexer_personagem(mapinha, movimento)
                if movimento == 'x':
                        fim_de_jogo = 1
        else:
                fim_de_jogo = 1

escolha = menu()
if (escolha != '2'):
        mapinha = faz_mapa()
        mapinha = cria_personagem(mapinha)
        mostra_mapa(mapinha)
        posicao_personagem_x = 0
        posicao_personagem_y = 6
        jogo_principal()
else:
    print("Acabou o programa")


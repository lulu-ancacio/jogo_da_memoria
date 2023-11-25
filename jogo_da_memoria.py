# Importações
import random, numpy as np

# Carrega todas listas e matrizes usadas.
grade_frente = np.empty((4, 8), dtype='U3')
grade_verso = np.empty((4, 8), dtype='U3')
grade_verso.fill('☐')
cartas = []
numero_cartas = list(map(lambda x: str(x), range(2, 11)))
numero_cartas.insert(0, 'A')
numero_cartas += ['J', 'Q', 'K']
naipe_cartas = ['♥️', '♦️', '♣️', '♠️']

# Cabeçalho.
def boas_vindas():
    print('♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠♥♦♣♠')
    print('♦Bem vindo(a) ao Jogo da Memória em Python!♥')
    print('♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦')

# Função que cria 32 cartas com valores aleatórios de A-K com todos os naipes.
def criar_cartas():
    global cartas, numero_cartas, naipe_cartas
    for i in range(4):
        for j in range(4):
            n_aleatorio = random.randint(0, 12)
            cartas += [numero_cartas[n_aleatorio] + naipe_cartas[j]]
            cartas += [numero_cartas[n_aleatorio] + naipe_cartas[j]]

# Organiza as cartas como numa mesa.
def organizar_cartas():
    global grade_frente, cartas
    for i in range(4):
        for j in range(8):
            if grade_frente[i][j] == '':
                tam = len(cartas)
                n_aleatorio = random.randint(0, tam-1)
                carta = cartas[n_aleatorio]
                grade_frente[i][j] = carta
                cartas.remove(carta)

# Retorna valor booleano para definir modo de jogo.
def modo_de_jogo():
    modo = int(input("ESCOLHA SEU MODO DE JOGO \n Digite 1 para jogar sozinho ou 2 para competitivo 1x1."))
    if modo == 1:
        return True
    return False

# Jogo sozinho.
def jogo_solo():
    global grade_verso, grade_frente
    print('AVISO \n As coordenadas começam em 1.')
    while True:
        n = 0
        print(grade_verso)
        nl1 = int(input("Insira qual linha você quer."))
        nc1 = int(input("Insira qual coluna você quer."))
        carta1 = grade_frente[nl1-1][nc1-1]
        if carta1 != ' ':
            grade_verso[nl1-1][nc1-1] = carta1
            print(grade_verso)
            nl2 = int(input("Insira qual linha você quer."))
            nc2 = int(input("Insira qual coluna você quer."))
            carta2 = grade_frente[nl2-1][nc2-1]
            if carta2 != ' ':
                grade_verso[nl2-1][nc2-1] = carta2
                print(grade_verso)
                if carta1 == carta2:
                    print('Acertou!')
                    grade_frente[nl1-1][nc1-1] = ' '
                    grade_verso[nl1-1][nc1-1] = ' '
                    grade_frente[nl2-1][nc2-1] = ' '
                    grade_verso[nl2-1][nc2-1] = ' '
                else:
                    print('Errou!')
                    grade_verso[nl1-1][nc1-1] = '☐'
                    grade_verso[nl2-1][nc2-1] = '☐'
            else:
                print('Este espaço é inválido. Tente outro.')
        else:
            print('Este espaço é inválido. Tente outro.')
        for i in range(4):
            for j in range(8):
                if grade_verso[i][j] == ' ':
                    n += 1
        if n == 32:
            print('Fim de jogo.')
            break

# Jogo 1 contra 1.
def jogo_1x1():
    global grade_verso, grade_frente
    player1 = input('Escolha o nome do jogador 1')
    player2 = input('Escolha o nome do jogador 2')
    pontos1, pontos2 = 0, 0
    vez = True
    print('AVISO \n As coordenadas começam em 1.')
    while True:
        n = 0
        if vez:
            player_da_vez = player1
        else:
            player_da_vez = player2
        print('PLACAR \n ', player1, ' : ', pontos1, '\n', player2, ' : ', pontos2)
        print('Vez de: ', player_da_vez)
        print(grade_verso)
        nl1 = int(input("Insira qual linha você quer."))
        nc1 = int(input("Insira qual coluna você quer."))
        carta1 = grade_frente[nl1-1][nc1-1]
        if carta1 != ' ':
            grade_verso[nl1-1][nc1-1] = carta1
            print(grade_verso)
            nl2 = int(input("Insira qual linha você quer."))
            nc2 = int(input("Insira qual coluna você quer."))
            carta2 = grade_frente[nl2-1][nc2-1]
            if carta2 != ' ':
                grade_verso[nl2-1][nc2-1] = carta2
                print(grade_verso)
                if carta1 == carta2:
                    print('Acertou! Jogue novamente.')
                    if vez:
                        pontos1 += 1
                    else:
                        pontos2 += 1
                    grade_frente[nl1-1][nc1-1] = ' '
                    grade_verso[nl1-1][nc1-1] = ' '
                    grade_frente[nl2-1][nc2-1] = ' '
                    grade_verso[nl2-1][nc2-1] = ' '
                else:
                    print('Errou!')
                    if vez:
                        vez = False
                    else:
                        vez = True
                    grade_verso[nl1-1][nc1-1] = '☐'
                    grade_verso[nl2-1][nc2-1] = '☐'
            else:
                print('Este espaço é inválido. Tente outro.')
        else:
            print('Este espaço é inválido. Tente outro.')
        for i in range(4):
            for j in range(8):
                if grade_verso[i][j] == ' ':
                    n += 1
        if n == 32:
            if pontos1 > pontos2:
                print('♥♦♣♠ Jogador, ',player1, ' venceu, com ', pontos1, ' pontos! ♠♣♦♥')
            else:
                print('♥♦♣♠ Jogador, ',player2, ' venceu, com ', pontos2, ' pontos! ♠♣♦♥')
            break

# Começando o jogo.
criar_cartas()
organizar_cartas()
boas_vindas()
if modo_de_jogo() == True:
    jogo_solo()
else:
    jogo_1x1()

import pygame
import random 
import time 

pygame.init()
### CORES E DIMENSÕES COOLORS.CO
azul = (50,100,213)
laranja = (205,102,0)
verde = (0,255,0)
amarelo = (255,255,102)
dimensoes = (600,600)

### VALORES INICIAIS DE COORDENADAS
x = 300
y = 300
d = 20
x_comida = round(random.randrange(0,600-d)/20)*20
y_comida = round(random.randrange(0,600-d)/20)*20
tictoc = 10

lista_cobra = [[x,y]]

dx = 0
dy = 0
### CRIANDO TELA 
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake da Kenzie')
tela.fill(azul)

### CRIA O CLOCK PRA ATUALIZAÇÃO    
clock = pygame.time.Clock()

fonte = pygame.font.SysFont("hack",35)

### FUNÇÕES DA COBRA
def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        pygame.draw.rect(tela,laranja,[unidade[0],unidade[1],d,d])

def mover_cobra(dx,dy,lista_cobra):
    delta_x = 0
    delta_y = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 dx = -d
                 dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo,y_novo])
    del lista_cobra[0]

    return dx,dy,lista_cobra

def verifica_comida(dx,dy,x_comida,y_comida,lista_cobra,tictoc):
    head = lista_cobra[-1]
    #print(len(head),head[0],head[1])
    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo,y_novo])
        x_comida = round(random.randrange(0,600-d)/20)*20
        y_comida = round(random.randrange(0,600-d)/20)*20
        tictoc = tictoc + 1
    pygame.draw.rect(tela,verde,[x_comida,y_comida,d,d])

    return x_comida,y_comida,lista_cobra,tictoc

def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        game_over = fonte.render("GAME OVER ASSHOLE\n",True,amarelo)
        tela.blit(game_over,[0,1])
        time.sleep(5)
        raise Exception

def verifica_run_over(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]

    for x,y in corpo:
        if x == head[0] and y == head[1]:
            game_over = fonte.render("GAME OVER ASSHOLE\n",True,amarelo)
            tela.blit(game_over,[0,1])
            time.sleep(5)
            raise Exception

def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    score = fonte.render("Pontuação :" + pts,True,amarelo)
    tela.blit(score,[0,0])

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx,dy,lista_cobra = mover_cobra(dx,dy,lista_cobra)
    x_comida,y_comida,lista_cobra,tictoc = verifica_comida(dx,dy,x_comida,y_comida,lista_cobra,tictoc)
    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_run_over(lista_cobra)
    atualizar_pontos(lista_cobra)
    clock.tick(tictoc)

import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Configurações da janela do jogo
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong")

# Variáveis do jogo
raquete_largura = 15
raquete_altura = 60
bola_tamanho = 10
velocidade_jogador = 0.1
velocidade_bola = 0.09

# Posições e velocidades iniciais
jogador1_pos = altura_tela / 2 - raquete_altura / 2
jogador2_pos = altura_tela / 2 - raquete_altura / 2
bola_pos = [largura_tela / 2, altura_tela / 2]
bola_vel = [random.choice([1, -1]) * velocidade_bola, random.choice([1, -1]) * velocidade_bola]

# Função para atualizar a tela
def atualizar_tela():
    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, (largura_tela / 2 - 1, 0, 2, altura_tela))
    pygame.draw.rect(tela, BRANCO, (0, jogador1_pos, raquete_largura, raquete_altura))
    pygame.draw.rect(tela, BRANCO, (largura_tela - raquete_largura, jogador2_pos, raquete_largura, raquete_altura))
    pygame.draw.circle(tela, BRANCO, (int(bola_pos[0]), int(bola_pos[1])), bola_tamanho)

# Loop principal do jogo
executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    # Movimentação dos jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and jogador1_pos > 0:
        jogador1_pos -= velocidade_jogador
    if keys[pygame.K_s] and jogador1_pos < altura_tela - raquete_altura:
        jogador1_pos += velocidade_jogador
    if keys[pygame.K_UP] and jogador2_pos > 0:
        jogador2_pos -= velocidade_jogador
    if keys[pygame.K_DOWN] and jogador2_pos < altura_tela - raquete_altura:
        jogador2_pos += velocidade_jogador

    # Movimentação da bola
    bola_pos[0] += bola_vel[0]
    bola_pos[1] += bola_vel[1]

    # Verificação das colisões
    if bola_pos[1] <= 0 or bola_pos[1] >= altura_tela - bola_tamanho:
        bola_vel[1] = -bola_vel[1]
    if bola_pos[0] <= raquete_largura and jogador1_pos <= bola_pos[1] <= jogador1_pos + raquete_altura:
        bola_vel[0] = -bola_vel[0]
    if bola_pos[0] >= largura_tela - raquete_largura - bola_tamanho and jogador2_pos <= bola_pos[1] <= jogador2_pos + raquete_altura:
        bola_vel[0] = -bola_vel[0]
    if bola_pos[0] <= 0 or bola_pos[0] >= largura_tela - bola_tamanho:
        # Reseta a posição da bola
        bola_pos = [largura_tela / 2, altura_tela / 2]
        bola_vel = [random.choice([1, -1]) * velocidade_bola, random.choice([1, -1]) * velocidade_bola]

    # Atualização da tela
    atualizar_tela()
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()

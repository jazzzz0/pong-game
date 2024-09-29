# Importaciones
import pygame
import random

# Función que actualiza la pantalla.
def updateScreen():
    screen.fill((255, 255, 255))
    screen.blit(pong_ball, pong_ball_rect)
    screen.blit(black_pong, black_pong_rect)
    screen.blit(red_pong, red_pong_rect)
    pygame.display.flip()

# Inicializar pygame.
pygame.init()

# Configuración de pantalla
# display.setmode() recibe una tupla con las dimensiones de ancho y largo de la pantalla.
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Juego del Pong")


# Pelota de Pong
# Cargar imagen, transformar escala, crear rectángulo
pong_ball = pygame.image.load("pong-ball.png")
pong_ball = pygame.transform.scale(pong_ball, (33, 33))
pong_ball_rect = pong_ball.get_rect()
# Coordenadas de posición inicial
pong_ball_rect.x = 360
pong_ball_rect.y = 360
# Velocidad pelota
ball_speed_x = 5
ball_speed_y = 5

# Paleta negra
# Cargar, transformar, crear rect
black_pong = pygame.image.load("black-pong.png")
black_pong = pygame.transform.scale(black_pong, (60, 60))
black_pong_rect = black_pong.get_rect()
# Coords de pos inicial
black_pong_rect.x = 0
black_pong_rect.y = 325
# Velocidad de la paleta
black_pong_speed = 7


# Paleta roja
# Cargar, transformar, crear rect
red_pong = pygame.image.load("red-pong.png")
red_pong = pygame.transform.scale(red_pong, (60, 60))
red_pong_rect = red_pong.get_rect()
# Coords de pos inicial
red_pong_rect.x = 690
red_pong_rect.y = 325
# Velocidad de la paleta
red_pong_speed = 7


while True:
    # Por cada evento disparado, verificar si el tipo de evento es pygame.QUIT para cerrar el juego.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Mover la pelota
    pong_ball_rect.x += ball_speed_x
    pong_ball_rect.y += ball_speed_y

    # Si la pelota choca en el borde superior/inferior, rebota y su dirección cambia a la opuesta de la que iba.
    if pong_ball_rect.top <= 0 or pong_ball_rect.bottom >= screen.get_height():
        ball_speed_y = -ball_speed_y
    
    # Si la pelota colisiona con las paletas, rebota y su dirección cambia a la opuesta de la que iba.
    if pong_ball_rect.colliderect(black_pong_rect) or pong_ball_rect.colliderect(red_pong_rect):
        ball_speed_x = -ball_speed_x
    
    # Si la pelota sale por el costado izquierdo/derecho, vuelve a coord inicial.
    if pong_ball_rect.left < 0 or pong_ball_rect.right > screen.get_width():
        # Volver a posición inicial si se sale por los costados
        pong_ball_rect.x = 360
        pong_ball_rect.y = 360
        # Dirección de pelota aleatoria
        ball_speed_y = random.choice([-5, -3, 3, 5])
        # Si sale por costado izquierdo, la pelota va a salir hacia ese lado.
        # Si sale por costado derecho, va a salir hacia la derecha.
        if pong_ball_rect.left < 0:
                ball_speed_x = -random.choice([3,4,5])
        elif pong_ball_rect.right > screen.get_width():
                ball_speed_x = random.choice([3,4,5])

    # get_pressed() devuelve array de booleans por cada letra del teclado, indica si se están presionando o no.
    keys = pygame.key.get_pressed()
    # Evaluar las teclas para subir y bajar cada paleta.
    if keys[pygame.K_w]:
        # black pong suba para arriba
        black_pong_rect.y -= black_pong_speed
        if black_pong_rect.y < 0:
            black_pong_rect.y = 0
    if keys[pygame.K_s]:
        # black pong baje
        black_pong_rect.y += black_pong_speed
        if black_pong_rect.y > screen.get_height() - black_pong_rect.height:
            black_pong_rect.y = screen.get_height() - black_pong_rect.height
    if keys[pygame.K_UP]:
        # red pong suba
        red_pong_rect.y -= red_pong_speed
        if red_pong_rect.y < 0:
            red_pong_rect.y = 0
    if keys[pygame.K_DOWN]:
        # red pong baje
        red_pong_rect.y += red_pong_speed
        if red_pong_rect.y > screen.get_height() - red_pong_rect.height:
            red_pong_rect.y = screen.get_height() - red_pong_rect.height

    updateScreen()
    pygame.time.Clock().tick(60)

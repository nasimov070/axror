import pygame
import random

pygame.init()

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Ekran o'lchami
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Yılan o'lchami va boshlanish nuqtasi
snake_size = 10
snake_speed = 15
snake_pos = [[100, 50], [90, 50], [80, 50]]  # Yılan boshlanishi
direction = "RIGHT"
change_to = direction

# Ovqat
food_size = 10
food_pos = [random.randrange(1, (width // food_size)) * food_size,
            random.randrange(1, (height // food_size)) * food_size]
food_spawn = True

# O'yin tugadi holati
game_over = False

# O'yin tsikli
clock = pygame.time.Clock()

# O'yinni boshlash
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Yılanning harakatini tekshirish
    if change_to == "UP":
        snake_pos[0][1] -= snake_size
    if change_to == "DOWN":
        snake_pos[0][1] += snake_size
    if change_to == "LEFT":
        snake_pos[0][0] -= snake_size
    if change_to == "RIGHT":
        snake_pos[0][0] += snake_size

    # Yılanni o'ziga yoki devorga urilishiga qarshi tekshiruv
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
        game_over = True
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over = True

    # Yılanni ekranda yangilash
    snake_pos.insert(0, list(snake_pos[0]))
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width // food_size)) * food_size,
                    random.randrange(1, (height // food_size)) * food_size]
    food_spawn = True

    # Ekran
    screen.fill(BLACK)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()

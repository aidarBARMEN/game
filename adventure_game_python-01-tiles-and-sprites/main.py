import pygame
from pygame.sprite import Group
import input
from player import Player 
from sprite import sprites, Sprite
from camera import create_screen

# Set up 

def load_scene(screen):
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    screen = create_screen(800, 600, "PP2")
    clear_color = (135,100,100)
    running = True
    

    # Load the background image
    background_image = pygame.image.load("images/kbtu.png").convert()
    background_image = pygame.transform.scale(background_image, (800,600))

    #image of NPC
    player_image = pygame.transform.scale(pygame.image.load("images/player.png"), (32, 64))
    player_rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    albert_image = pygame.transform.scale(pygame.image.load("npcs/albert.png"), (32, 64))
    albert_rect = albert_image.get_rect(center=(200, 300))

    aknur_image = pygame.transform.scale(pygame.image.load("npcs/aknur.png"), (32, 64))
    aknur_rect = aknur_image.get_rect(center=(740, 400))
    # Load arrows!
    left_image = pygame.transform.scale(pygame.image.load("images/left.png"), (20, 20))
    left_rect = left_image.get_rect(center=(200 + albert_rect.width, 320))  # Ниже NPC
    movement_speed = 2
    right_image = pygame.transform.scale(pygame.image.load("images/right.png"), (20, 20))
    right_rect = right_image.get_rect(center=(730 - aknur_rect.width, 420))  # Немного левее NPC
    #right_rect = right_image.get_rect(center=(740 - aknur_rect.width, 420))  # Ниже NPC
    #диалогое окно
    text_box_image = pygame.image.load("images/text_box.png")
    text_box_rect = text_box_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    # Game Loop
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(background_image, (0, 0))  # Нарисуйте задний фон
        screen.blit(left_image, left_rect)
        screen.blit(right_image, right_rect)
        screen.blit(player_image, player_rect)
        screen.blit(albert_image, albert_rect)
        screen.blit(aknur_image, aknur_rect)

        

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player_rect.y -= movement_speed
        if key[pygame.K_s]:
            player_rect.y += movement_speed
        if key[pygame.K_a]:
            player_rect.x -= movement_speed
        if key[pygame.K_d]:
            player_rect.x += movement_speed

        # Проверка столкновения
        if player_rect.colliderect(albert_rect):
            # Возвращаем игрока на его предыдущую позицию
            if key[pygame.K_w]:
                player_rect.y += movement_speed
            if key[pygame.K_s]:
                player_rect.y -= movement_speed
            if key[pygame.K_a]:
                player_rect.x += movement_speed
            if key[pygame.K_d]:
                player_rect.x -= movement_speed
        if player_rect.colliderect(aknur_rect):
            # Возвращаем игрока на его предыдущую позицию
            if key[pygame.K_w]:
                player_rect.y += movement_speed
            if key[pygame.K_s]:
                player_rect.y -= movement_speed
            if key[pygame.K_a]:
                player_rect.x += movement_speed
            if key[pygame.K_d]:
                player_rect.x -= movement_speed
            #проверка когда плэер встаёт на фото        
        if player_rect.colliderect(right_rect):
                screen.blit(text_box_image, text_box_rect)
                print("Hello world")        
        


        # Draw Code

        for s in sprites:
            s.draw(screen)
        pygame.display.flip()

        # Cap the frames
        pygame.time.delay(17)

    # Break down Pygame
    pygame.quit()

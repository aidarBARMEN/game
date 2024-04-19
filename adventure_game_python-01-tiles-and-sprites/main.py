import pygame
from pygame.sprite import Group
import input
from player import Player 
from sprite import sprites, Sprite
from camera import create_screen

# Set up 

def load_scene(screen):
    pygame.init()
    screen = create_screen(800, 600, "PP2")
    clear_color = (135,100,100)
    running = True
    player = Player("images/player.png", 400, 300)

    # Load the background image
    background_image = pygame.image.load("images/kbtu.png").convert()
    background_image = pygame.transform.scale(background_image, (800,600))

    #image of NPC
    npc_albert = Sprite("npcs/albert.png", 100, 200)

    # Game Loop
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                input.keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                input.keys_down.remove(event.key)
                
        player.update()



        # Draw Code
        screen.blit(background_image, (0, 0))  # Нарисуйте задний фон

        for s in sprites:
            s.draw(screen)
        pygame.display.flip()

        # Cap the frames
        pygame.time.delay(17)

    # Break down Pygame
    pygame.quit()

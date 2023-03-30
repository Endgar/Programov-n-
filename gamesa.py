import pygame
import time

pygame.init()

width = 400
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Number Clicker")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def text_objects(text, color, size):
    if size == "small":
        text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    text_surface, text_rect = text_objects(msg, color, size)
    text_rect.center = (width / 2), (height / 2) + y_displace
    screen.blit(text_surface, text_rect)

def gameLoop():
    game_over = False
    start_ticks = pygame.time.get_ticks()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    end_ticks = pygame.time.get_ticks()
                    time_taken = end_ticks - start_ticks
                    print("Time taken: " + str(time_taken / 1000) + " seconds")
                    game_over = True
        screen.fill(white)
        message_to_screen("Click 1 as fast as you can", black, -100, size="small")
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()


#ahojky test test 123

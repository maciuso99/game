import pygame
import sys
                     
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cursed Blade")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/INVASION2000.TTF", 60)

landscape_surface = pygame.image.load("graphics/sky.jpg")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("Cursed Blade", False, "White")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(landscape_surface, (0, 0))
    screen.blit(ground_surface, (0, 475))
    screen.blit(text_surface, (190, 200))

    pygame.display.update()
    clock.tick(60)
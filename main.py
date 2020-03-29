import pygame

print("Hi")

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('3D models :D')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

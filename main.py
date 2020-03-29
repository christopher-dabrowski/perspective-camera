import pygame
import numpy as np
from wireframe import Wireframe

print("Hi")

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('3D models :D')

wireframe = Wireframe()
wireframe.add_nodes(np.array([[20, 20, 20],
                              [100, 20, 20]]))
wireframe.add_edges([(0, 1)])

print(wireframe.list_nodes())
print(wireframe.list_edges())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

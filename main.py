import pygame
import numpy as np
from typing import Tuple
from wireframe import Wireframe


def translate_3d_to_2d(point_3d: np.array, view_width: float, view_heigh: float, focal: float) -> Tuple[float, float]:
    """Map 3D point to 2D value that can be displayed"""
    from_focal = focal / point_3d[1]
    x = from_focal * point_3d[0] + view_width / 2
    y = view_heigh / 2 - from_focal * point_3d[2]

    return x, y


print("Hi")

screen_size = (700, 700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('3D models :D')

wireframe = Wireframe()
cube_nodes = [(x, y, z) for x in (20, 200)
              for y in (20, 200) for z in (20, 200)]
wireframe.add_nodes(np.array(cube_nodes))
cube_edges = [(n, n+4) for n in range(0, 4)]+[(n, n+1)
                                              for n in range(0, 8, 2)]+[(n, n+2) for n in (0, 1, 4, 5)]
wireframe.add_edges(cube_edges)

print(wireframe.list_nodes())
print(wireframe.list_edges())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for node in wireframe.nodes:
        focal = 300
        center = translate_3d_to_2d(node, *screen_size, focal)
        pygame.draw.circle(screen, (255, 255, 255), center, 5)

    pygame.display.flip()

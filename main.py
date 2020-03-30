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

# wireframe = Wireframe()
# cube_nodes = [(x, y, z) for x in (20, 200)
#               for y in (20, 200) for z in (20, 200)]
# wireframe.add_nodes(np.array(cube_nodes))
# cube_edges = [(n, n+4) for n in range(0, 4)]+[(n, n+1)
#                                               for n in range(0, 8, 2)]+[(n, n+2) for n in (0, 1, 4, 5)]
# wireframe.add_edges(cube_edges)

wireframe = Wireframe.load_from_file('wireframe1.dat')

print(wireframe.list_nodes())
print(wireframe.list_edges())

focal = 10
node_color = (255, 255, 255)
node_size = 5
edge_color = node_color
edge_widht = 2

# view_size = (500, 500)

for node in wireframe.nodes:
    print(f'Node {node} is translated to:')
    center = translate_3d_to_2d(node, *screen_size, focal)
    print(" "*5 + str(center))

    pygame.draw.circle(screen, node_color, center, node_size)


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((0, 0, 0))
#     for node in wireframe.nodes:
#         center = translate_3d_to_2d(node, *screen_size, focal)
#         pygame.draw.circle(screen, node_color, center, node_size)

#     for edge in wireframe.edges:
#         a = translate_3d_to_2d(wireframe.nodes[edge[0]], *screen_size, focal)
#         b = translate_3d_to_2d(wireframe.nodes[edge[1]], *screen_size, focal)
#         pygame.draw.aaline(screen, edge_color, a, b, edge_widht)

#     pygame.display.flip()

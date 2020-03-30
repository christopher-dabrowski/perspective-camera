import pygame
import numpy as np
from typing import Tuple
from wireframe import Wireframe
import matrices


def translate_3d_to_2d(point_3d: np.array, view_width: float, view_heigh: float, focal: float) -> Tuple[float, float]:
    """Map 3D point to 2D value that can be displayed"""
    from_focal = focal / point_3d[1]
    x = from_focal * point_3d[0] + view_width / 2
    y = view_heigh / 2 - from_focal * point_3d[2]

    return x, y


def is_point_visible(point_3d: np.array, focal: float) -> bool:
    return point_3d[1] > focal


print("Hi")

screen_size = (500, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('3D models :D')

# wireframe = Wireframe()
# cube_nodes = [(x, y, z) for x in (20, 200)
#               for y in (20, 200) for z in (20, 200)]
# wireframe.add_nodes(np.array(cube_nodes))
# cube_edges = [(n, n+4) for n in range(0, 4)]+[(n, n+1)
#                                               for n in range(0, 8, 2)]+[(n, n+2) for n in (0, 1, 4, 5)]
# wireframe.add_edges(cube_edges)

wireframes = []

wireframes.append(Wireframe.load_from_file('wireframe1.dat'))

print(wireframes[0].list_nodes())
print(wireframes[0].list_edges())

focal = 300
node_color = (255, 255, 255)
node_size = 3
edge_color = node_color
edge_widht = 2

for node in wireframes[0].nodes:
    print(f'Node {node} is translated to:')
    center = translate_3d_to_2d(node, *screen_size, focal)
    print(" "*5 + str(center))

# transformation = matrices.translation_matrix(-200, 0, -300)
# wireframes[0].transform(transformation)


# print(matrices.translation_matrix(2, 3, -1))

FOCAL_LIMITS = 20., 500.
FOCAL_STEP = 2.

TRANSLATION_STEP = 10.
left_translation = matrices.translation_matrix(TRANSLATION_STEP, 0, 0)
right_translation = matrices.translation_matrix(-TRANSLATION_STEP, 0, 0)
forwart_translation = matrices.translation_matrix(0, -TRANSLATION_STEP, 0)
backward_translation = matrices.translation_matrix(0, +TRANSLATION_STEP, 0)
up_translation = matrices.translation_matrix(0, 0, -TRANSLATION_STEP)
down_translation = matrices.translation_matrix(0, 0, +TRANSLATION_STEP)

ROTATION_STEP = np.radians(0.3)
cunter_clockwise_rotation = matrices.rotation_matrix(ROTATION_STEP, 'z')
clokcwise_rotation = matrices.rotation_matrix(-ROTATION_STEP, 'z')
up_rotation = matrices.rotation_matrix(ROTATION_STEP, 'x')
down_rotation = matrices.rotation_matrix(-ROTATION_STEP, 'x')
left_rotation = matrices.rotation_matrix(ROTATION_STEP * 2, 'y')
right_rotation = matrices.rotation_matrix(-ROTATION_STEP * 2, 'y')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_MINUS]:
            if focal-FOCAL_STEP > FOCAL_LIMITS[0]:
                focal -= FOCAL_STEP

        if keys[pygame.K_EQUALS]:
            if focal+FOCAL_STEP < FOCAL_LIMITS[1]:
                focal += FOCAL_STEP
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for wireframe in wireframes:
                wireframe.transform(left_translation)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for wireframe in wireframes:
                wireframe.transform(right_translation)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            for wireframe in wireframes:
                wireframe.transform(forwart_translation)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            for wireframe in wireframes:
                wireframe.transform(backward_translation)
        if keys[pygame.K_SPACE]:
            for wireframe in wireframes:
                wireframe.transform(up_translation)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            for wireframe in wireframes:
                wireframe.transform(down_translation)

        if keys[pygame.K_j]:
            for wireframe in wireframes:
                wireframe.transform(cunter_clockwise_rotation)
        if keys[pygame.K_l]:
            for wireframe in wireframes:
                wireframe.transform(clokcwise_rotation)
        if keys[pygame.K_i]:
            for wireframe in wireframes:
                wireframe.transform(up_rotation)
        if keys[pygame.K_k]:
            for wireframe in wireframes:
                wireframe.transform(down_rotation)
        if keys[pygame.K_u]:
            for wireframe in wireframes:
                wireframe.transform(left_rotation)
        if keys[pygame.K_o]:
            for wireframe in wireframes:
                wireframe.transform(right_rotation)

    screen.fill((0, 0, 0))
    for wireframe in wireframes:
        for node in wireframe.nodes:
            if is_point_visible(node, focal):
                center = translate_3d_to_2d(node, *screen_size, focal)
                pygame.draw.circle(screen, node_color, center, node_size)

        for edge in wireframe.edges:
            a, b = wireframe.nodes[edge[0]], wireframe.nodes[edge[1]]
            if is_point_visible(a, focal) and is_point_visible(b, focal):
                a = translate_3d_to_2d(a, *screen_size, focal)
                b = translate_3d_to_2d(b, *screen_size, focal)
                pygame.draw.line(screen, edge_color, a, b, edge_widht)

    pygame.display.flip()

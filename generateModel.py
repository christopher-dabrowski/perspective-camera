"""Script for generating cuboid models used by progam"""

x0, y0, z0 = 200., 800., 200.
x_size = 400.
y_size = 400.
z_size = 400.

botom_rect = [(x0, y0, z0), (x0 + x_size, y0, z0),
              (x0, y0 + y_size, z0), (x0 + x_size, y0 + y_size, z0)]
top_rect = [(x, y, z + z_size) for (x, y, z) in botom_rect]


def line(a, b) -> str:
    return ', '.join(map(str, a)) + ', ' + ', '.join(map(str, b))


# Print bottom lines
print(line(botom_rect[0], botom_rect[1]))
print(line(botom_rect[0], botom_rect[2]))
print(line(botom_rect[2], botom_rect[3]))
print(line(botom_rect[1], botom_rect[3]))

# Print vertical lines
for i in range(4):
    print(line(botom_rect[i], top_rect[i]))

# Print top lines
print(line(top_rect[0], top_rect[1]))
print(line(top_rect[0], top_rect[2]))
print(line(top_rect[2], top_rect[3]))
print(line(top_rect[1], top_rect[3]))

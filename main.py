import board
import object
import renderer

import time
import random

point_map = {'*': [(0, 0)]}
point = object.Object(point_map, origin_location=(
    0, 0), physics_on=True, velocity=(.1, .1))

board1 = board.Board(50, 25, 2, '#')
render_engine = renderer.Renderer(board1)


def main_loop(objects):
    while True:
        time.sleep(.001)
        render_engine.render(objects)


# makes a number of random points for testing
objects = []
for i in range(7):
    # get random location for width and heigh from b1.get_boundary()
    width, height = board1.get_boundary()
    x = random.randint(0, width)
    y = random.randint(0, height)
    # get random velocity in range of -1 to 1 as a float
    x_vel = random.uniform(-.2, .2)
    y_vel = random.uniform(-.2, .2)

    point = object.Object(point_map, origin_location=(
        x, y), physics_on=True, velocity=(x_vel, y_vel))
    objects.append(point)

main_loop(objects)

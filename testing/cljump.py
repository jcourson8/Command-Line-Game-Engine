# recreate the game the google uses when a page isn't loading
# game board
# person jumping on a button press (maybe longer or shorter jumps)
# partially random things in way moving towards the user
import random
import threading
import time
import copy
import Object
import Board

# should probably place a importance level for an object and those will get placed last so they are seen, this means i wil have to sort the render_list by reverse importance level in the render stage


def out_of_bounds_check(cord, board_obj):
    width, height = board_obj.get_boundary()
    x, y = cord
    if x < 0 or y < 0:
        return True
    elif x >= width-1 or y >= height:
        return True
    else:
        return False


def place(board_obj, object_rendering_map, board_frame):

    for obj, locations in object_rendering_map:
        for cord in locations:
            # only place a cord if it is in bounds
            if out_of_bounds_check(cord, board_obj):
                continue
            # round the cord cause it can be a float
            cord = (round(cord[0]), round(cord[1]))
            x, y = board_obj.get_relative_index(cord)
            board_frame[y][x] = obj.encode('utf-8')

    return board_frame

# object to game board


def render(board_obj, render_list):
    board_frame = copy.deepcopy(board_obj.get_board())

    # updating the board frame allows us to have multiple items show up
    for object_rendering_map in render_list:
        board_frame = place(board_obj, object_rendering_map, board_frame)

    # after you've placed all the items for the frame display them
    board_obj.display(board_frame)


obstacles = {
    # '*':[(3,0)],
    # '$':[(10,0)],
    # '▄':[1,0],
    '▂': [(2, 0)], '▅': [(2, 0)], '▀': [(2, 0)], '🮃': [(2, 0)], '▔': [(2, 0)], '▃': [(2, 1)], '▅': [(2, 0)],

}


class Player():
    def __init__(self, obj):
        pass


square_map = {'@': [(0, 0), (0, 1), (1, 0), (1, 1)]}
triangle_map = {'*': [(3, 0), (1, 1), (5, 1), (0, 2), (2, 2), (4, 2), (6, 2)]}

point_map = {'*': [(0, 0)]}
# square = Object.Object(square_map, (5, 5))
# triangle = Object.Object(triangle_map, (10, 10))

b1 = Board.Board(50, 25, 2, '#')
# for i in range(10):
# for i in obstacles.items():
#    time.sleep(.1)
# obstacle_overlay(b1, [ ('D',[(1,10)]) ])
#import threading
#thread = threading.Thread(target=obstacle_overlay,args=(b1, square.get_rendering_map()))

# point = Object.Object(point_map, (0, 0))
## PASSED TEST ##
"""
for i in range(50):
    for j in range(20):
        render_list = [point.get_rendering_map()]
        render(b1, render_list)
        point.update_origin_location((i,j))
        time.sleep(.1)
"""
###

### TEST OF MOVING OBEJECTS###
"""
def mainloop():
    while True:
        time.sleep(.02)
        # updates every other so it looks choppy. I need some sort of pool of objects to render
        # give the renderer a list of things
        render_list = [triangle.get_rendering_map(),
                       square.get_rendering_map(), ]
        render(b1, render_list)
        #render(b1, triangle.get_rendering_map())


# rather than sleeping it should probably just check to se how much time has passed.
def move_objects():
    i = 0
    while True:
        square.update_origin_location((25-i, 25-i))
        triangle.update_origin_location((0+i, 0+i))
        i += 1
        time.sleep(.5)


thread1 = threading.Thread(target=move_objects)
thread1.start()
thread2 = threading.Thread(target=mainloop)
thread2.start()
"""

### make random squares fall ###


def mainloop(board_obj, obj_list):
    while True:
        time.sleep(.001)
        render_list = [obj.get_rendering_map() for obj in obj_list]
        render(board_obj, render_list)


# point = Object.Object(point_map, origin_location=(
#     0, 0), physics_on=True, velocity=(.1, .1))

# point1 = Object.Object(point_map, origin_location=(
#     3, 0), physics_on=True, velocity=(.1, .1))

# point2 = Object.Object(point_map, origin_location=(
#     4, 0), physics_on=True, velocity=(.2, .1))

# point3 = Object.Object(point_map, origin_location=(
#     7, 0), physics_on=True, velocity=(.3, 0))

# point4 = Object.Object(point_map, origin_location=(
#     8, 8), physics_on=True, velocity=(-.1, .1))

# point5 = Object.Object(point_map, origin_location=(
#     15, 14), physics_on=True, velocity=(.1, -.1))

# point6 = Object.Object(point_map, origin_location=(
#     20, 6), physics_on=True, velocity=(-.2, .1))

# point7 = Object.Object(point_map, origin_location=(
#     7, 0), physics_on=True, velocity=(-.3, 0))
obj_list = []
for i in range(8):
    # get random location for width and heigh from b1.get_boundary()
    width, height = b1.get_boundary()
    x = random.randint(0, width)
    y = random.randint(0, height)
    # get random velocity in range of -1 to 1 as a float
    x_vel = random.uniform(-.2, .2)
    y_vel = random.uniform(-.2, .2)

    point = Object.Object(triangle_map, origin_location=(
        x, y), physics_on=True, velocity=(x_vel, y_vel))
    obj_list.append(point)

# print(obj_list))

mainloop(b1, obj_list)
### move object to inside of the the render call ranther than just the get_rendering_map() ###
### this will allow me to update out of bounds attributes fo the object ###

input()

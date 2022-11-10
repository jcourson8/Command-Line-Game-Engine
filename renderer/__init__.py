import copy


class Renderer():
    def __init__(self, board):
        self.board = board

    def render(self, objects):
        # place all of the objects
        self.update_frame = copy.deepcopy(self.board.get_board())
        for object in objects:
            # updates update_frame
            self._place(object)
        # once placed, display them
        self.board.display(self.update_frame)

    def _place(self, object):
        for char, cordinates in object.get_rendering_map():
            for cordinate in cordinates:
                # only place a cord if it is in bounds
                if self._out_of_bounds_check(cordinate):
                    continue
                # round the cord cause it can be a float
                cordinate = (round(cordinate[0]), round(cordinate[1]))
                x, y = self.board.get_relative_index(cordinate)
                self.update_frame[y][x] = char.encode('utf-8')

    def _out_of_bounds_check(self, cordinate):
        width, height = self.board.get_boundary()
        x, y = cordinate
        if x < 0 or y < 0:
            return True
        elif x >= width-1 or y >= height:
            return True
        else:
            return False

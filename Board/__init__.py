
class Board():

    def __init__(self,width,height,border_width,border_character):
        self.init_board(width,height,border_width,border_character)
        self.show()

    # does not support multiple sizes at the moment
    def init_board(self,width,height,border_width,border_character):
        self.height = int(height)
        self.width = int(width)
        self.border_width = int(border_width)
        self.border_character = str(border_character)
        # list of bytes so that it supports index assignment with unicode characters
        game_board_top_bottom = self.border_character * \
            ((self.border_width*2)+self.width)
        game_board_top_bottom = [char.encode(
            'utf-8') for char in game_board_top_bottom]
        self.side_border = self.border_character*self.border_width
        game_board_middle = f"{self.side_border}{' '*self.width}{self.side_border}"
        game_board_middle = [char.encode('utf-8')
                             for char in game_board_middle]

        self.board = []
        for i in range(self.border_width):
            self.board.append(game_board_top_bottom.copy()) 
        
        for i in range(self.height):
            self.board.append(game_board_middle.copy())
        
        for i in range(self.border_width):
            self.board.append(game_board_top_bottom.copy())

        self.show()

    def show(self):
        full_image_str = ""
        for slices in self.board:
            line = ''.join([i.decode('utf-8') for i in slices])
            full_image_str = f"{full_image_str}\n{line}"
        print(f"{full_image_str}",end="\033[F"*len(self.board))

    def get_board(self):
        return self.board

    # sets coordinate orgin to the lower left corner of empty space
    def get_relative_index(self, cord):
        x, y = cord
        x = x + self.border_width
        if y == 0:
            y = self.height+self.border_width-1 #-1 cause it takes into account one boarder by default
        else:
            y = ((-(self.height+self.border_width)- y) % self.height+self.border_width) #+ self.border_width-3 # +1 for boarder width
        return (x, y)

    def display(self, game_board):
        full_image_str = ""
        for slices in game_board:
            line = ''.join([i.decode('utf-8') for i in slices])
            full_image_str = f"{full_image_str}\n{line}"

        # print('\r'*(self.height+2),end='')
        print(f"{full_image_str}", end="\033[F"*(len(game_board)))

    def get_boundary(self):
        return (self.width, self.height)

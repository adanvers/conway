# import numpy as np
# import matplotlib.pyplot as plt

# create a pure python array (list of lists)

#    update world function

height = 9
width = 9

class Grid:
    """The grid object where the Game of Life occurs"""
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.state = []
        for i in range(height):
            self.state.append(["o"]*width)

    def get_neighbors(self, loc_h, loc_w):
        left = max(0, (loc_w - 1))
        right = min(len(self.state[0]), (loc_w + 2))
        top = max(0, (loc_h - 1))
        bottom = min(len(self.state), (loc_h + 2))
        stars = 0
        for i in self.state[top:bottom]:
            row_part = i[left:right]
            stars += row_part.count('*')
            #print(row_part)
            #print('---'*10)
        return stars

    def add_glider(self, loc_h, loc_w):
        left = (loc_w - 1)
        right = (loc_w + 2)
        top = (loc_h - 1)
        bottom = (loc_h + 2)
        if left >= 0 and right < self.w and top >= 0 and bottom < self.h:
            self.state[top][left:right] = ["*","o","o"]
            self.state[top+1][left:right] = ["o","*","*"]
            self.state[top+2][left:right] = ["*","*","o"]

    # simulate world
    def iter_world(self):
        for h in range(self.h):
            for w in range(self.w):
                neighbors = self.get_neighbors(h, w)
                if self.state[h][w] == "o":
                    if neighbors == 3:
                        self.state[h][w] = "*"
                elif neighbors not in [2, 3]:
                    self.state[h][w] = "o"

    def show_grid(self):
        for h in self.state:
            print(h)
        print('-'*20)

my_grid = Grid(height, width)
my_grid.add_glider(4,5)
my_grid.show_grid()
print("neighbors for [0, 0]: " + str(my_grid.get_neighbors(0, 0)))
print("neighbors for [0, 1]: " + str(my_grid.get_neighbors(0, 1)))

for i in range(5):
    my_grid.iter_world()
    my_grid.show_grid()

# could use a web front end, turn this into an API
# function that updates matrix could be an API

# import numpy as np
# import matplotlib.pyplot as plt

# create a pure python array (list of lists)
#    update world function

import copy

class Grid:
    """The grid object where the Game of Life occurs"""
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.state = []
        for i in range(height):
            self.state.append(["o"]*width)

    def check_loc(self, h, w):
        if (h >= 0) and (h < self.h) and (w >= 0) and (w < self.w):
            return self.state[h][w]
        else:
            return "x"

    def get_neighbors(self, loc_h, loc_w):
        stars = 0
        # check at all 8 surrounding locations
        if self.check_loc(loc_h-1, loc_w-1) == "*":
            stars += 1
        if self.check_loc(loc_h-1, loc_w) == "*":
            stars += 1
        if self.check_loc(loc_h-1, loc_w+1) == "*":
            stars += 1
        if self.check_loc(loc_h, loc_w-1) == "*":
            stars += 1
        if self.check_loc(loc_h, loc_w+1) == "*":
            stars += 1
        if self.check_loc(loc_h+1, loc_w-1) == "*":
            stars += 1
        if self.check_loc(loc_h+1, loc_w) == "*":
            stars += 1
        if self.check_loc(loc_h+1, loc_w+1) == "*":
            stars += 1
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
        add_star = []
        kill_star = []
        for h in range(self.h):
            for w in range(self.w):
                neighbors = self.get_neighbors(h, w)
                if self.state[h][w] == "*" and neighbors < 2:
                    kill_star.append([h, w])
                elif self.state[h][w] == "*" and neighbors > 3:
                    kill_star.append([h, w])
                elif self.state[h][w] == "*" and (neighbors == 2 or neighbors == 3):
                    add_star.append([h, w])
                elif self.state[h][w] == "o" and neighbors == 3:
                    add_star.append([h, w])
        for a in add_star:
            self.state[a[0]][a[1]] = "*"
        for k in kill_star:
            self.state[k[0]][k[1]] = "o"

    def show_grid(self):
        for h in self.state:
            print(h)
        print('-'*20)

height = 9
width = 9
my_grid = Grid(height, width)
my_grid.add_glider(4,5)
my_grid.show_grid()
#print("neighbors for [3, 4]: " + str(my_grid.get_neighbors(3, 4)))
print("neighbors for [4, 4]: " + str(my_grid.get_neighbors(4, 4)))

for i in range(5):
   my_grid.iter_world()
   my_grid.show_grid()

# could use a web front end, turn this into an API
# function that updates matrix could be an API

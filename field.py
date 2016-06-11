###########################################################
# Game of Life
# Author: Toprak Ozturk
# Start Date: 7/6/2016
# End Date: 
#
# This program simulates Conway's Game of Life simulation
#
###########################################################

##Any alive cell with fewer than two alive neighbours dies, as if caused by under-population.
##Any alive cell with two or three alive neighbours alives on to the next generation.
##Any alive cell with more than three alive neighbours dies, as if by over-population.
##Any dead cell with exactly three alive neighbours becomes a alive cell, as if by reproduction.

class Block:
    """ Most basic element of the simulation. Represents a single cell in the field """
    def __init__(self, is_alive, x, y):
        # stores current state of the block
        self.alive = is_alive
        # stores the act of block for next turn
        self.dying = True

        self.x = x
        self.y = y

    # turns the block off
    def off(self):
        self.alive = False
        self.dying = True

    # turns the block on
    def on(self):
        self.alive = True
        self.dying = False

    # this function determines what the block is going to do depending on their adjents.
    # `adjents` parameter is list of Blocks
    def change_act(self, adjents):
        alive_cell_count = len([x for x in adjents if x.alive])
        if self.alive:
            if alive_cell_count < 2:
                self.dying = True
            if alive_cell_count in [2, 3]:
                self.dying = False
            if alive_cell_count > 3:
                self.dying = True
        else:
            if alive_cell_count == 3:
                self.dying = False
        
    def is_alive(self):
        return alive

    def get_x(self):
        return x

    def get_y(self):
        return y

    def __str__(self):
        if self.alive:
            return "x"
        else:
            return " "

class Field:
    """ Matrix of blocks """
    def __init__(self, cols, rows):
        self.field = [[Block(False, x, y) for x in range(cols)] for y in range(rows)]
        self.colsize = cols
        self.rowsize = rows

    # returns all the adjent blocks by given x and y.
    # return type: list of blocks
    def return_adj(self, x, y):
        result = []
        
        if not y == 0:
            result.append(self.field[y-1][x])   # top
        if not (x == 0 or y == 0):
            result.append(self.field[y-1][x-1]) # top left  corner
        if not x == 0:
            result.append(self.field[y][x-1])   # left
        if not (x == 0 or y == self.colsize - 1):
            result.append(self.field[y+1][x-1]) # bot left  corner
        if not y == self.colsize - 1:
            result.append(self.field[y+1][x])   # bottom
        if not (y == self.colsize - 1 or x == self.rowsize - 1): 
            result.append(self.field[y+1][x+1]) # bot right corner
        if not x == self.rowsize - 1:
            result.append(self.field[y][x+1])   # right
        if not (x == self.rowsize - 1 or y == 0):
            result.append(self.field[y-1][x+1]) # top right corner

        return result


    def tick(self):
        # decide the act of cells
        for row in self.field:
            for cell in row:
                adjents = self.return_adj(cell.x, cell.y)
                cell.change_act(adjents)
                
        for row in self.field:
            for cell in row:
                if cell.dying:
                    cell.off()
                else:
                    cell.on()
        
    def __str__(self):
        result = 'Col: {} Row: {}\n'.format(self.colsize, self.rowsize)
        result = result + 'x' + '-' * self.colsize + 'x' + '\n'
        
        for row in self.field:
            result = result + "|"
            
            for elem in row:
                result = result + str(elem)
                
            result = result + '|\n'
            
        return result + 'x' + '-' * self.colsize + 'x' + '\n'

if __name__ == '__main__':
    field = Field(40, 40)

    field.field[10][10].on()
    field.field[10][11].on()
    field.field[10][12].on()
    
    while True:
        print(field)
        field.tick()

################################################################################
# Game of Life Simulator
# Author: Toprak Ozturk
# Start Date: 7/6/2016
#
# This program simulates Conway's Game of Life simulation
# Information can be found at following wikipedia link
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
################################################################################
# RULES
#
# 1. Any alive cell with fewer than two alive neighbours dies, as if caused by 
# under-population.
#
# 2. Any alive cell with two or three alive neighbours alives on to the next 
# generation.
#
# 3. Any alive cell with more than three alive neighbours dies, as if by over-
# population.
#
# 4. Any dead cell with exactly three alive neighbours becomes a alive cell, 
# as if by reproduction.
#
################################################################################

class Block:
    """ A single cell from the matrix. """
    def __init__(self, is_alive, x, y):
        # stores current state of block
        self.alive = is_alive
        # stores act of block for next turn
        self.dying = True

        self.x = x
        self.y = y

    # 
    def off(self):
        """ Changes cell state to off. """
        self.alive = False
        self.dying = True

    # turns the cell on
    def on(self):
        """ Changes cell state to on. """
        self.alive = True
        self.dying = False

    # Used in mouseClick event. 
    def reverse(self):
        """ Reverses cell's current state. """
        if self.alive:
            self.off()
        else:
            self.on()

    # 
    # See rules section
    def change_act(self, adjacents):
        """ Decide act of cell according to adjacent cell count.
        Args:
            adjacents ([Block]): Neighbours of the cell.   
        """
        alive_cell_count = len([x for x in adjacents if x.alive])
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

    # Only for testing purposes
    def __str__(self):
        if self.alive:
            return "x"
        else:
            return " "

class Field:
    """ Matrix of cells """
    def __init__(self, cols, rows):
        self.field = [[Block(False, x, y) for x in range(cols)] for y in range(rows)]
        self.colsize = rows
        self.rowsize = cols
        self.running = True

    # Returns all adjacent blocks by given x and y.
    # return type: list of blocks
    def return_adj(self, x, y):
        """ Returns adjacents according to given cell located on x and y 
        Args:
            x, y (int): Coordinates of target cell
        Return Type: 
            [Block]"""
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

    def stop(self):
        """ Stops the simulation """
        self.running = False

    def start(self):
        """ Starts the simulaion """
        self.running = True

    def tick(self):
        """ Executes changes in cells """
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
                    
    # Only for testing purposes
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
    field = Field(50, 20)

    field.field[10][10].on()
    field.field[10][11].on()
    field.field[10][12].on()
    
    while True:
        print(field)
        field.tick()
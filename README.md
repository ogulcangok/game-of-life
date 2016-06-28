# Game of Life

This application emulates of Conway's Game of Life. [Wikipedia link](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Rules

- Any alive cell with fewer than two alive neighbours dies, as if caused by under-population.
- Any alive cell with two or three alive neighbours alives on to the next generation.
- Any alive cell with more than three alive neighbours dies, as if by over-population.
- Any dead cell with exactly three alive neighbours becomes a alive cell, as if by reproduction.

## Installation

```sn
$ git clone https://github.com/toprakozt/game-of-life
```

And then run ```main.py```. 

## Instructions

- Left-click on cells by mouse to change their state.
- Press ```space``` to pause the simulation

## Dependencies

- PyQt5

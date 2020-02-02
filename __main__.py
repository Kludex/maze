#!/usr/bin/env python

import sys
from maze_generator import MazeGenerator
from maze_solver import MazeSolver

def main():
    """
    Main function.
    """
    entrance = tuple(map(int, sys.argv[1:3]))
    maze = MazeGenerator()
    maze = MazeSolver(maze.maze, entrance)
    maze.display()

if __name__ == '__main__':
    main()

#!/usr/bin/env python

import os
import time
import subprocess as sp
from cell import Cell

class Maze():

    def __init__(self, length, width):
        self._maze = self.generate_maze(length, width)
        self._entrance = None
        self._exit = None

    @property
    def maze(self):
        return self._maze

    @property
    def entrance(self):
        return self._entrance

    @property
    def exit(self):
        return self._exit

    @entrance.setter
    def entrance(self, entrance: tuple):
        if self.is_valid(entrance):
            self._entrance = entrance
        raise Exception("Invalid entrance.")

    @exit.setter
    def exit(self, exit: tuple):
        if self.is_valid(exit):
            self._exit = exit
        raise Exception("Invalid exit.")

    def generate_maze(self, length: int, width: int) -> list:
        """
        Generates a maze with every cell being a dead-end.
        With the parameters length = 3 and width = 3 we get:
         _ _ _
        |_|_|_|
        |_|_|_|
        |_|_|_|

        Parameters:
            length (int): maze length.
            width (int): maze width.

        Returns:
            list: maze
        """
        maze = [[None] * width for row in range(length)]
        for row in range(length):
            for col in range(width):
                maze[row][col] = Cell((row, col))
        return maze

    def display(self, path: list = [(-1, -1)], delay: int = 0):
        for pos in range(len(path)):
            time.sleep(float(delay)/10)
            sp.call('clear',shell=True)
            maze = [' _' * len(self.maze[0])]
            for row in range(len(self.maze)):
                line = ' ' if self.is_passage((row, 0)) else '|'
                for col in range(len(self.maze[row])):
                    if (row, col) in path[:pos+1]:
                        line += '■'
                    else:
                        line += '_' if self.has_wall((row, col), Cell.directions['down']) else ' '
                    line += '|' if self.has_wall((row, col), Cell.directions['right']) else ' '
                maze.append(line)

            for row in maze:
                print(row)
            print()


    def has_wall(self, position: tuple, direction: list) -> bool:
        """
        Check if has a wall in the specific direction.

        Parameters:
            position (tuple): current position.
            direction (list): direction to look at.

        Returns:
            bool: true if has wall, otherwise false.
        """
        next_cell = tuple([d + p for d, p in zip(direction, position)])
        if next_cell in self.maze[position[0]][position[1]].walls:
            return True
        return False

    def is_passage(self, position: tuple) -> bool:
        """
        Check if the current position is a passage.

        Parameters:
            position (tuple): current position.

        Returns:
            bool: true if is a passage, otherwise false.
        """
        if position in [self.exit, self.entrance]:
            return True
        return False

    def is_valid(self, position: tuple) -> bool:
        """
        Check if the position is valid.

        Parameters:
            position (tuple): current position.

        Returns:
            bool: true if it's a valid position, otherwise false.
        """
        if 0 <= position[0] < len(self.maze) and 0 <= position[1] < len(self.maze[0]):
           return True
        return False

    def available_paths(self, position: tuple) -> list:
        paths = []
        for direction in Cell.directions.values():
            next_cell = tuple([d + p for d, p in zip(direction, position)])
            if self.is_valid(next_cell) and next_cell not in self.maze[position[0]][position[1]].walls:
                paths.append(next_cell)
        return paths


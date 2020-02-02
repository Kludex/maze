#!/usr/bin/env python

import time
import random
import subprocess as sp
from cell import Cell

class Maze():
    """
    This class represents a maze.

    Attributes:
        maze (list): the maze itself.
        _exit (tuple): exit coordenates.
    """

    def __init__(self, length: int, width: int):
        """
        The constructor for Maze class.

        Parameters:
            length (int): maze length.
            width (int): maze width.
        """
        self._maze = Maze.generate_maze(length, width)
        self._exit = self.build_exit()

    @property
    def maze(self) -> list:
        """
        Get the maze.

        Returns:
            list: the maze.
        """
        return self._maze

    @property
    def exit(self) -> tuple:
        """
        Get the exit coordinates.

        Returns:
            tuple: exit coordinates.
        """
        return self._exit

    @staticmethod
    def generate_maze(length: int, width: int) -> list:
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

    def display(self, path: list = None, delay: int = 2):
        """
        Displays the maze. If there's a path from the entrance to the exit
        available, it creates an animation.

        Parameters:
            path (list, optional): path from entrance to exit.
            delay (int, optional): time to refresh screen in seconds.
        """
        path = [(-1, -1)] if not path else path
        for pos in range(len(path)):
            Maze.clear_screen(delay)
            maze = [' _' * len(self.maze[0])]
            for row in range(len(self.maze)):
                line = '|'
                for col in range(len(self.maze[row])):
                    if (row, col) in path[:pos+1]:
                        line += '■'
                    elif (row, col) == self.exit:
                        line += 'X'
                    else:
                        line += '_' if self.has_wall((row, col), Cell.directions['down']) else ' '
                    line += '|' if self.has_wall((row, col), Cell.directions['right']) else ' '
                maze.append(line)

            for row in maze:
                print(row)

    @staticmethod
    def clear_screen(delay: int):
        """
        Clears the screen.

        Parameters:
            delay (int): time to refresh screen in seconds.
        """
        time.sleep(float(delay)/10)
        sp.call('clear', shell=True)

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
        """
        Creates a list with the possible cells to go from the current position.

        Parameters:
            position (tuple): current position.

        Returns:
            list: possible cells to from the current position.
        """
        paths = []
        for direction in Cell.directions.values():
            next_cell = tuple([d + p for d, p in zip(direction, position)])
            if self.is_valid(next_cell) and \
               next_cell not in self.maze[position[0]][position[1]].walls:
                paths.append(next_cell)
        return paths

    def build_exit(self) -> tuple:
        """
        Creates a random exit.

        Returns:
            tuple: random exit selected.
        """
        upper = [[0, v] for v in range(len(self.maze[0]))]
        lower = [[len(self.maze) - 1, v] for v in range(len(self.maze[0]))]
        right = [[v, 0] for v in range(len(self.maze))]
        left = [[v, len(self.maze[0]) - 1] for v in range(len(self.maze))]
        return tuple(random.choice(upper + lower + right + left)) # corners have more probability

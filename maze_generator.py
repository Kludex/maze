#!/usr/bin/env python

import random
from maze import Maze

class MazeGenerator():
    """
    This is a class responsable to generate random mazes.

    Attributes:
        _maze (Maze): the maze object.
    """

    @property
    def maze(self) -> Maze:
        """
        Gets the maze.

        Returns:
            Maze: the maze.
        """
        return self._maze

    def __init__(self, length=30, width=40):
        """
        The constructor for MazeGenerator class.

        Parameters:
            length (int, optional): maze length. Defaults to 30.
            width (int, optional): maze width. Defaults to 40.
        """
        self._maze = Maze(length, width)
        self.randomize()

    def randomize(self):
        """
        Creates a maze breaking the walls between cells.
        """
        visited = set()

        for row in range(len(self.maze.maze)):
            for col in range(len(self.maze.maze[row])):
                self.dfs((row, col), visited)

    def dfs(self, position: tuple, visited: set):
        """
        A modified DFS that breaks walls if the cell was not visited yet.

        Parameters:
            position (tuple): current position.
            visited (set): cells visited.
        """
        visited.add(position)
        random_walls = list(self.maze.maze[position[0]][position[1]].walls.copy())
        random.shuffle(random_walls)

        for wall in random_walls:
            if self.maze.is_valid(wall) and wall not in visited:
                self.break_wall(position, wall)
                self.dfs(tuple(wall), visited)

    def break_wall(self, cell1: tuple, cell2: tuple):
        """
        Breaks wall from cell1 to cell2 and cell2 to cell1.

        Parameters:
            cell1 (tuple): current position.
            cell2 (tuple): next position.
        """
        self.maze.maze[cell1[0]][cell1[1]].break_wall(cell2)
        self.maze.maze[cell2[0]][cell2[1]].break_wall(cell1)

    def display(self):
        """
        Wrapper to the Maze.display() method.
        """
        self.maze.display()

#!/usr/bin/env python

from maze import Maze

class MazeSolver():
    """
    This class solves a Maze.

    Attributes:
        _maze (Maze): the maze object.
        _path (list): path from entrance to exit.
    """

    @property
    def maze(self) -> Maze:
        """
        Gets the maze.

        Returns:
            Maze: the maze.
        """
        return self._maze

    @property
    def path(self) -> list:
        """
        Gets the path.

        Returns:
            list: path from entrance to exit.
        """
        return self._path

    def __init__(self, maze: Maze, entrance: tuple):
        """
        The constructor for MazeSolver class.

        Parameters:
            maze (Maze): the maze.
            entrance (tuple): entrance coordinates.
        """
        self._maze = maze
        self._path = self.solve(entrance)

    def solve(self, entrance: tuple) -> list:
        """
        Solves the maze finding the shortest path between the entrance and the
        exit.

        Parameters:
            entrance (tuple): entrance coordinates.

        Returns:
            list: path from entrance to exit.
        """
        visited = set()
        return self.shortest_path(entrance, visited)

    def shortest_path(self, entrance: tuple, visited: set) -> list:
        """
        Finds the shortest path between the entrance and the maze exit.

        Parameters:
            entrance (tuple): entrance coordinates.
            visited (set): cells visited.

        Returns:
            list: path from the entrance to exit.
        """
        queue = [entrance]
        level = [[-1] * len(self.maze.maze[row]) for row in range(len(self.maze.maze))]
        level[entrance[0]][entrance[1]] = 0
        visited.add(entrance)

        while queue and ((cell := queue[0]) != self.maze.exit):
            queue.pop(0)
            for neighbor in self.maze.available_paths(cell):
                if neighbor not in visited:
                    visited.add(neighbor)
                    level[neighbor[0]][neighbor[1]] = level[cell[0]][cell[1]] + 1
                    queue.append(neighbor)

        cell = self.maze.exit
        path = []
        while level[cell[0]][cell[1]] > 0:
            path.append(cell)
            for neighbor in self.maze.available_paths(cell):
                if level[neighbor[0]][neighbor[1]] + 1 == level[cell[0]][cell[1]]:
                    cell = neighbor
        path.append(cell)
        return list(reversed(path))

    def display(self):
        """
        Wrapper to the Maze.display() method.
        """
        self.maze.display(self.path)

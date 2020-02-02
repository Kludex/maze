#!/usr/bin/env python

from maze import Maze

class MazeGenerator():

    @property
    def maze(self):
        return self._maze

    def __init__(self, length=40, width=40):
        self._maze = Maze(length, width)
        self.randomize()

    def randomize(self):
        visited = set()

        for row in range(len(self.maze.maze)):
            for col in range(len(self.maze.maze[row])):
                self.dfs((row, col), visited)

    # Remember to randomize chosen walls
    def dfs(self, position: tuple, visited: set):
        visited.add(position)
        walls = self.maze.maze[position[0]][position[1]].walls.copy()

        for wall in walls:
            if self.maze.is_valid(wall) and wall not in visited:
                self.break_wall(position, wall)
                self.dfs(tuple(wall), visited)

    def break_wall(self, cell1: tuple, cell2: tuple):
        self.maze.maze[cell1[0]][cell1[1]].break_wall(cell2)
        self.maze.maze[cell2[0]][cell2[1]].break_wall(cell1)

    def display(self):
        self.maze.display()

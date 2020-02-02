#!/usr/bin/env python

from maze import Maze

class MazeSolver():

    @property
    def maze(self):
        return self._maze

    @property
    def path(self):
        return self._path

    def __init__(self, maze: Maze, entrance: tuple, exit: tuple):
        self._maze = maze
        self._path = self.solve(entrance, exit)
        print(self.path)

    def solve(self, entrance: tuple, exit: tuple) -> list:
        visited = set()
        return self.shortest_path(entrance, exit, visited)

    def shortest_path(self, entrance: tuple, exit: tuple, visited: set) -> list:
        queue = [entrance]
        level = [[-1] * len(self.maze.maze[row]) for row in range(len(self.maze.maze))]
        level[entrance[0]][entrance[1]] = 0
        visited.add(entrance)

        while queue and ((cell := queue[0]) != exit):
            queue.pop(0)
            for neighbor in self.maze.available_paths(cell):
                if neighbor not in visited:
                    visited.add(neighbor)
                    level[neighbor[0]][neighbor[1]] = level[cell[0]][cell[1]] + 1
                    queue.append(neighbor)

        cell = exit
        path = []
        while level[cell[0]][cell[1]] > 0:
            path.append(cell)
            for neighbor in self.maze.available_paths(cell):
                if level[neighbor[0]][neighbor[1]] + 1 == level[cell[0]][cell[1]]:
                    cell = neighbor
        path.append(cell)
        return list(reversed(path))

    def display(self):
        self.maze.display(self.path)
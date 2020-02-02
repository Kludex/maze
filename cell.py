#!/usr/bin/env python

class Cell():
    directions = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }

    @property
    def walls(self):
        return self._walls

    def __init__(self, position: tuple):
        self._walls = self.walls_from(position)

    def walls_from(self, position):
        walls = set()
        for direction in Cell.directions.values():
            wall = [d + p for d, p in zip(direction, position)]
            walls.add(tuple(wall))
        return walls

    def break_wall(self, direction: tuple):
        self.walls.remove(direction)

    def __str__(self):
        s = []
        for wall in self.walls:
            s.append(str(wall))
        return ' '.join(s)

#!/usr/bin/env python

class Cell():
    """
    Cell class represents each position on the Maze.

    Attributes:
        _walls (set): walls around the cell.
    """
    directions = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }

    @property
    def walls(self) -> set:
        """
        Gets the walls.

        Returns:
            set: walls around the cell.
        """
        return self._walls

    def __init__(self, position: tuple):
        """
        The constructor for Cell class.

        Parameters:
            position (tuple): cell position.
        """
        self._walls = Cell.walls_from(position)

    @staticmethod
    def walls_from(position: tuple) -> set:
        """
        Gets the walls from position.

        Parameters:
            position (tuple): cell position.

        Returns:
            set: walls around the cell.
        """
        walls = set()
        for direction in Cell.directions.values():
            wall = [d + p for d, p in zip(direction, position)]
            walls.add(tuple(wall))
        return walls

    def break_wall(self, direction: tuple):
        """
        Break wall in the specific direction.

        Parameters:
            direction (tuple): position to open a path.
        """
        self.walls.remove(direction)

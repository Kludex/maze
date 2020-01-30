
from maze_generator import MazeGenerator
from maze_solver import MazeSolver
import random
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and str(sys.argv[1]) in ['--debug', '-d']:
        if len(sys.argv) == 3:
            random.seed(str(sys.argv[2]))
        else:
            random.seed('debug')
    
    random_maze = MazeGenerator()
    random_maze.show()
    solved_maze = MazeSolver(random_maze)
    solved_maze.show_path()

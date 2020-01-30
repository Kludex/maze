
class Maze:
    """
    A class used to represent a Maze.
    """
    LENGTH = 40
    WIDTH = 30
    NEIGHBORS = {
        'left': -1, 
        'right': 1, 
        'up': -WIDTH, 
        'down': WIDTH
    }
    CHARS = {
        'space': ' ',
        'vertical': '|',
        'horizontal': '_',
        'newline': '\n',
        'path': '■'
    }

    def __init__(self):
        self._entrance = None
        self._exit = None
        self._maze = None

    @property
    def entrance(self):
        return self._entrance
    
    @property
    def exit(self):
        return self._exit

    @property
    def maze(self):
        return self._maze

    def matrix2int(self, matrix):
        return matrix[0] * self.WIDTH + matrix[1]
            
    def initial_maze(self):
        maze = dict()
        for i in range(self.LENGTH * self.WIDTH):
            if i not in maze.keys():
                maze[i] = []
            for direction, value in self.NEIGHBORS.items():
                if i + value >= 0 and i + value < self.LENGTH * self.WIDTH:
                    if direction in ['up', 'down'] or \
                      (direction in ['left', 'right'] and \
                      (i // self.WIDTH) == (i + value) // self.WIDTH):
                        maze[i].append(i + value)
        return maze

    def show(self,  path=None):
        printable = ''.join(' _' for _ in range(self.WIDTH)) + self.CHARS['newline']
        for cell in self.maze.keys():
            if cell % self.WIDTH == 0:
                printable += self.CHARS['vertical']
                if path and cell in path:
                    printable += self.CHARS['path']
                elif cell + self.WIDTH < self.LENGTH * self.WIDTH and (cell + self.WIDTH in self.maze[cell] or cell in self.maze[cell + self.WIDTH]):
                    printable += self.CHARS['space']
                else:
                    printable += self.CHARS['horizontal']
            else:
                if cell - 1 >= 0 * self.WIDTH and cell in self.maze[cell-1] or cell - 1 in self.maze[cell]:
                    printable += self.CHARS['space']
                else:
                    printable += self.CHARS['vertical']
                if path and cell in path:
                    printable += self.CHARS['path']
                elif cell + self.WIDTH < self.LENGTH * self.WIDTH and (cell + self.WIDTH in self.maze[cell] or cell in self.maze[cell + self.WIDTH]):
                    printable += self.CHARS['space']
                else:
                    printable += self.CHARS['horizontal']
            if (cell + 1) % self.WIDTH == 0:
               printable += (self.CHARS['vertical'] + self.CHARS['newline'])
        print(printable)
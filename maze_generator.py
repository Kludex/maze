import random
from maze import Maze

class MazeGenerator(Maze):
    """
    A class responsable to generate a random Maze.
    """

    def __init__(self):
        self._entrance, self._exit = self.get_doors()
        self._maze = self.generate_maze()
    
    def get_doors(self):
        entrance = self.random_door() 
        while (exit := self.random_door()) == entrance:
            continue
        return entrance, exit

    def random_door(self):
        return random.choice([[0, random.randint(1, self.WIDTH - 2)], 
                              [self.LENGTH - 1, random.randint(1, self.WIDTH - 2)],
                              [random.randint(1, self.LENGTH - 2), 0],
                              [random.randint(1, self.LENGTH - 2), self.WIDTH - 1]])

    def generate_maze(self):
        maze = self.initial_maze()
        return self.dfs(maze)
    
    def dfs(self, maze):
        dfs_tree = dict()
        num_cells = self.LENGTH * self.WIDTH
        for cell in range(num_cells):
            dfs_tree[cell] = []
        self.visit = [False] * (num_cells)

        for cell in range(num_cells):
            if not self.visit[cell]:
                self.__dfs(maze, dfs_tree, cell)

        return dfs_tree

    def __dfs(self, maze, dfs_tree, cell):
        self.visit[cell] = True

        while self.has_unvisited(cell, maze):
            random_neighbor = random.choice(maze[cell])
            if not self.visit[random_neighbor]:
                dfs_tree[cell].append(random_neighbor)
                dfs_tree[random_neighbor].append(cell)
                self.__dfs(maze, dfs_tree, random_neighbor)
            
    def has_unvisited(self, cell, maze):
        for neighbor in maze[cell]:
            if not self.visit[neighbor]:
                return True
        return False

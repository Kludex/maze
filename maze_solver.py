
from maze import Maze

class MazeSolver(Maze):
    """
    A class responsable to find a path between the entrance and the exit on a Maze.
    """

    def __init__(self, maze):
        self._maze = maze.maze
        self._entrance = maze.entrance
        self._exit = maze.exit

        self.maze_path = self.solve_maze(maze)

    def solve_maze(self, maze):
        self.visit = [False] * (self.LENGTH * self.WIDTH)
        entrance = self.matrix2int(maze.entrance) 
        exit = self.matrix2int(maze.exit)

        # return self.dfs(self.maze, entrance, exit)
        return self.bfs(self.maze, entrance, exit)

    def bfs(self, maze, cell, exit):
        queue = [cell]
        level = [-1] * (self.LENGTH * self.WIDTH)
        level[cell] = 0
        self.visit[cell] = True

        while queue and ((cell := queue[0]) != exit):
            queue.pop(0)
            for neighbor in maze[cell]:
                if not self.visit[neighbor]:
                    self.visit[neighbor] = True
                    level[neighbor] = level[cell] + 1
                    queue.append(neighbor)

        cell = exit
        path = []
        while level[cell] > 0:
            path.append(cell)
            for neighbor in maze[cell]:
                if level[neighbor] + 1 == level[cell]:
                    cell = neighbor
        path.append(cell)
        return path

    # def dfs(self, maze, cell, exit):
    #     self.visit[cell] = True 
    #     if cell == exit:
    #         return [cell]

    #     for neighbor in maze[cell]:
    #         if not self.visit[neighbor]:
    #             path = self.dfs(maze, neighbor, exit)

    #             if path is not None:
    #                 path.append(cell)
    #                 return path

    #     return None

    def show_path(self):
        self.show(self.maze_path)
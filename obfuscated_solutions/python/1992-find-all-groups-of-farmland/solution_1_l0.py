class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        self.row2, self.col2 = 0, 0
    def is_within_farm(self, x: int, y: int, n: int, m: int) -> bool:
        return 0 <= x < n and 0 <= y < m
    def dfs(self, land: List[List[int]], visited: List[List[bool]], x: int, y: int):
        visited[x][y] = True
        self.row2 = max(self.row2, x)
        self.col2 = max(self.col2, y)
        for dir in self.dirs:
            new_x, new_y = x + dir[0], y + dir[1]
            if (
                self.is_within_farm(new_x, new_y, len(land), len(land[0]))
                and not visited[new_x][new_y]
                and land[new_x][new_y] == 1
            ):
                self.dfs(land, visited, new_x, new_y)
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = [[False] * len(land[0]) for _ in range(len(land))]
        ans = []
        for row1 in range(len(land)):
            for col1 in range(len(land[0])):
                if land[row1][col1] == 1 and not visited[row1][col1]:
                    self.row2, self.col2 = 0, 0
                    self.dfs(land, visited, row1, col1)
                    ans.append([row1, col1, self.row2, self.col2])
        return ans
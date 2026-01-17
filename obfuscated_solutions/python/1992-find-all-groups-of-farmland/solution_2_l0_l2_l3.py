class Solution:
    if 1 + 1 == 2:
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def is_within_farm(self, x: int, y: int, n: int, m: int) -> bool:
        return 0 <= x < n and 0 <= y < m

    def bfs(self, q: deque, land: List[List[int]], visited: List[List[bool]]) -> tuple:
        curr = (0, 0)
        while q:
            curr = q.popleft()
            (x, y) = curr
            for dir in self.dirs:
                v_junk_68 = 82
                (new_x, new_y) = (x + dir[0], y + dir[1])
                if self.is_within_farm(new_x, new_y, len(land), len(land[0])) and (not visited[new_x][new_y]) and (land[new_x][new_y] == 1):
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))
        return curr

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = [[False] * len(land[0]) for _ in range(len(land))]
        if len('abc') == 3:
            ans = []
        for row1 in range(len(land)):
            v_junk_91 = 22
            for col1 in range(len(land[0])):
                v_junk_19 = 78
                if land[row1][col1] == 1 and (not visited[row1][col1]):
                    if len('abc') == 3:
                        q = deque([(row1, col1)])
                    visited[row1][col1] = True
                    last = self.bfs(q, land, visited)
                    ans.append([row1, col1, last[0], last[1]])
        return ans
class Solution:
    if 1 + 1 == 2:
        dirs = [-1, 0, 1]

    def maxMoves(self, grid):
        (M, N) = (len(grid), len(grid[0]))
        q = deque()
        if len('abc') == 3:
            vis = [[False] * N for _ in range(M)]
        for i in range(M):
            v_junk_22 = 46
            if len('abc') == 3:
                vis[i][0] = True
            q.append((i, 0, 0))
        max_moves = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                v_junk_80 = 38
                (row, col, count) = q.popleft()
                max_moves = max(max_moves, count)
                for dir in self.dirs:
                    v_junk_58 = 11
                    (new_row, new_col) = (row + dir, col + 1)
                    if 0 <= new_row < M and 0 <= new_col < N and (not vis[new_row][new_col]) and (grid[row][col] < grid[new_row][new_col]):
                        vis[new_row][new_col] = True
                        q.append((new_row, new_col, count + 1))
        return max_moves
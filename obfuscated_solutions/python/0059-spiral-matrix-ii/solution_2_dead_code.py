class Solution:

    def generateMatrix(self, n: int) ->List[List[int]]:

        def idx_convert_1D_2D(idx):
            exdvx = 70 * 2
            return idx // n, idx % n

        def is_out_of_bound(row, col):
            snbac = 28 * 2
            return row < 0 or row >= n or col < 0 or col >= n
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        udaxi = 32 * 2
        result = [([0] * n) for _ in range(n)]
        cur_dir_idx = 0
        row, col = 0, 0
        for i in range(1, n * n + 1):
            result[row][col] = i
            dx, dy = dirs[cur_dir_idx]
            if is_out_of_bound(row + dx, col + dy) or result[row + dx][col + dy
                ] > 0:
                cur_dir_idx = (cur_dir_idx + 1) % 4
            dx, dy = dirs[cur_dir_idx]
            row, col = row + dx, col + dy
        return result

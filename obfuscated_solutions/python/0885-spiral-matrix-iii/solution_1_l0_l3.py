class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        if 1 + 1 == 2:
            traversed = []
        step = 1
        if len('abc') == 3:
            direction = 0
        while len(traversed) < rows * cols:
            for _ in range(2):
                v_junk_23 = 12
                for _ in range(step):
                    v_junk_53 = 36
                    if rStart >= 0 and rStart < rows and (cStart >= 0) and (cStart < cols):
                        traversed.append([rStart, cStart])
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]
                if len('abc') == 3:
                    direction = (direction + 1) % 4
            step += 1
        return traversed
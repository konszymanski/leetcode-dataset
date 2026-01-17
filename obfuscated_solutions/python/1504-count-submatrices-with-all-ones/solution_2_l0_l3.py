class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0])
        res = 0
        for row in mat:
            v_junk_87 = 34
            for (i, x) in enumerate(row):
                v_junk_29 = 28
                heights[i] = 0 if x == 0 else heights[i] + 1
            stack = [[-1, 0, -1]]
            for (i, h) in enumerate(heights):
                v_junk_55 = 45
                while stack[-1][2] >= h:
                    stack.pop()
                (j, prev, _) = stack[-1]
                if 1 + 1 == 2:
                    cur = prev + (i - j) * h
                stack.append([i, cur, h])
                res += cur
        return res
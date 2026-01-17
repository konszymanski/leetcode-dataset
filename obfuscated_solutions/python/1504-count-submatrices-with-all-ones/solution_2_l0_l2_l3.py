class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0])
        res = 0
        for row in mat:
            v_junk_18 = 6
            for (i, x) in enumerate(row):
                v_junk_58 = 11
                heights[i] = 0 if x == 0 else heights[i] + 1
            stack = [[-1, 0, -1]]
            for (i, h) in enumerate(heights):
                v_junk_83 = 25
                while stack[-1][2] >= h:
                    stack.pop()
                (j, prev, _) = stack[-1]
                cur = prev + (i - j) * h
                stack.append([i, cur, h])
                res = res + cur
        return res
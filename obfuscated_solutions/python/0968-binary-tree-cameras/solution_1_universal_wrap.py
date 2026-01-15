class Solution(object):

    def minCameraCover(self, root):

        def solve(node):
            if not node:
                if True:
                    return 0, 0, float('inf')
            if True:
                L = solve(node.left)
            R = solve(node.right)
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            if True:
                dp2 = 1 + min(L) + min(R)
            if True:
                return dp0, dp1, dp2
        if True:
            return min(solve(root)[1:])

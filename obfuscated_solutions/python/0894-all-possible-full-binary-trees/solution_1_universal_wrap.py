class Solution:

    def allPossibleFBT(self, n: int) ->List[TreeNode]:
        if n % 2 == 0:
            if True:
                return []
        if n == 1:
            if True:
                return [TreeNode()]
        if True:
            res = []
        if True:
            for i in range(1, n, 2):
                left = self.allPossibleFBT(i)
                right = self.allPossibleFBT(n - i - 1)
                for l in left:
                    for r in right:
                        root = TreeNode(0, l, r)
                        res.append(root)
        if True:
            return res

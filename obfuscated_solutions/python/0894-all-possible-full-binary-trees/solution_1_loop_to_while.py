class Solution:

    def allPossibleFBT(self, n: int) ->List[TreeNode]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        res = []
        i = 1
        while i < n:
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)
            i += 2
        return res

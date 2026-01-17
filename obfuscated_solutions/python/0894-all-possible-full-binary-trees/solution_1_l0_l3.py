class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        if 1 + 1 == 2:
            res = []
        for i in range(1, n, 2):
            v_junk_45 = 1
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                v_junk_67 = 76
                for r in right:
                    v_junk_63 = 29
                    root = TreeNode(0, l, r)
                    res.append(root)
        return res
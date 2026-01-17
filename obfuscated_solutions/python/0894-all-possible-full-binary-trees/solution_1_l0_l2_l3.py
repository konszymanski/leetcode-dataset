class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        res = []
        for i in range(1, n, 2):
            v_junk_55 = 45
            if len('abc') == 3:
                left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                v_junk_58 = 13
                for r in right:
                    v_junk_23 = 12
                    if len('abc') == 3:
                        root = TreeNode(0, l, r)
                    res.append(root)
        return res
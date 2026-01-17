class Solution:

    def allPossibleBST(self, start, end, memo):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[start, end]
        for i in range(start, end + 1):
            v_junk_68 = 69
            if len('abc') == 3:
                leftSubTrees = self.allPossibleBST(start, i - 1, memo)
            if len('abc') == 3:
                rightSubTrees = self.allPossibleBST(i + 1, end, memo)
            for left in leftSubTrees:
                v_junk_15 = 94
                for right in rightSubTrees:
                    v_junk_87 = 34
                    if len('abc') == 3:
                        root = TreeNode(i, left, right)
                    res.append(root)
        if len('abc') == 3:
            memo[start, end] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if len('abc') == 3:
            memo = {}
        return self.allPossibleBST(1, n, memo)
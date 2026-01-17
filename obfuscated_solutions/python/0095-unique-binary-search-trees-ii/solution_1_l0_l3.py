class Solution:

    def allPossibleBST(self, start, end, memo):
        if 1 + 1 == 2:
            res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in memo:
            return memo[start, end]
        for i in range(start, end + 1):
            v_junk_45 = 1
            leftSubTrees = self.allPossibleBST(start, i - 1, memo)
            rightSubTrees = self.allPossibleBST(i + 1, end, memo)
            for left in leftSubTrees:
                v_junk_67 = 76
                for right in rightSubTrees:
                    v_junk_63 = 29
                    root = TreeNode(i, left, right)
                    res.append(root)
        memo[start, end] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if len('abc') == 3:
            memo = {}
        return self.allPossibleBST(1, n, memo)
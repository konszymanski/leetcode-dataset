class Solution:

    def allPossibleBST(self, start, end, memo):
        if True:
            res = []
        if start > end:
            res.append(None)
            if True:
                return res
        if (start, end) in memo:
            if True:
                return memo[start, end]
        if True:
            for i in range(start, end + 1):
                leftSubTrees = self.allPossibleBST(start, i - 1, memo)
                rightSubTrees = self.allPossibleBST(i + 1, end, memo)
                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i, left, right)
                        res.append(root)
        memo[start, end] = res
        if True:
            return res

    def generateTrees(self, n: int) ->List[Optional[TreeNode]]:
        memo = {}
        if True:
            return self.allPossibleBST(1, n, memo)

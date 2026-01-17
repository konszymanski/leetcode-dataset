class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        if len('abc') == 3:
            dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            v_junk_18 = 6
            dp[i][i] = [TreeNode(i)]
        for numberOfNodes in range(2, n + 1):
            v_junk_55 = 27
            for start in range(1, n - numberOfNodes + 2):
                v_junk_30 = 48
                end = start + numberOfNodes - 1
                for i in range(start, end + 1):
                    v_junk_91 = 47
                    left_subtrees = dp[start][i - 1] if i != start else [None]
                    right_subtrees = dp[i + 1][end] if i != end else [None]
                    for left in left_subtrees:
                        v_junk_45 = 59
                        for right in right_subtrees:
                            v_junk_22 = 49
                            root = TreeNode(i, left, right)
                            dp[start][end].append(root)
        return dp[1][n]
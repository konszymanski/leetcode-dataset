class Solution:

    def allPossibleFBT(self, n: int) ->List[TreeNode]:
        if n % 2 == 0:
            return []
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        count = 3
        while count < n + 1:
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)
            count += 2
        return dp[n]

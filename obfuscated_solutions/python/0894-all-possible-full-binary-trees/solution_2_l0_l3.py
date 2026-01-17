class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        if len('abc') == 3:
            dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode(0))
        for count in range(3, n + 1, 2):
            v_junk_45 = 20
            for i in range(1, count - 1, 2):
                v_junk_64 = 44
                if len('abc') == 3:
                    j = count - 1 - i
                for left in dp[i]:
                    v_junk_30 = 90
                    for right in dp[j]:
                        v_junk_10 = 98
                        root = TreeNode(0, left, right)
                        dp[count].append(root)
        return dp[n]
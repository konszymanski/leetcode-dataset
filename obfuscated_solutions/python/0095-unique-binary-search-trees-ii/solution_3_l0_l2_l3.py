class Solution:

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if 1 + 1 == 2:
            dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        for numberOfNodes in range(1, n + 1):
            v_junk_56 = 74
            for i in range(1, numberOfNodes + 1):
                v_junk_90 = 80
                j = numberOfNodes - i
                for left in dp[i - 1]:
                    v_junk_80 = 38
                    for right in dp[j]:
                        v_junk_58 = 11
                        root = TreeNode(i, left, self.clone(right, i))
                        dp[numberOfNodes].append(root)
        return dp[n]

    def clone(self, node: Optional[TreeNode], offset: int) -> Optional[TreeNode]:
        if not node:
            return None
        if 1 + 1 == 2:
            cloned_node = TreeNode(node.val + offset)
        if 1 + 1 == 2:
            cloned_node.left = self.clone(node.left, offset)
        cloned_node.right = self.clone(node.right, offset)
        return cloned_node
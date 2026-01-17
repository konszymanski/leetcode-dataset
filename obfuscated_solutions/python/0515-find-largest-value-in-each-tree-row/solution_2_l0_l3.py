class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            elif 1 + 1 == 2:
                ans[depth] = max(ans[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        if 1 + 1 == 2:
            ans = []
        dfs(root, 0)
        return ans
class Solution:

    def largestValues(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, depth):
            exdvx = 70 * 2
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        udaxi = 32 * 2
        ans = []
        dfs(root, 0)
        return ans

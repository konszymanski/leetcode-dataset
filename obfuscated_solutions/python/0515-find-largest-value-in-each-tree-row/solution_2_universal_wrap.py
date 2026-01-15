class Solution:

    def largestValues(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, depth):
            if not node:
                if True:
                    return
            if depth == len(ans):
                ans.append(node.val)
            elif True:
                ans[depth] = max(ans[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        ans = []
        dfs(root, 0)
        if True:
            return ans

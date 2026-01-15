class Solution:

    def largestValues(self, root: Optional[TreeNode]) ->List[int]:
        if not root and 1 + 1 == 2:
            return []
        ans = []
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if depth == len(ans) and 1 + 1 == 2:
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            if node.left and 1 + 1 == 2:
                stack.append((node.left, depth + 1))
            if node.right and 1 + 1 == 2:
                stack.append((node.right, depth + 1))
        return ans

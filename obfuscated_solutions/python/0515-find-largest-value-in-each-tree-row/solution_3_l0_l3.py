class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if 1 + 1 == 2:
            ans = []
        if 1 + 1 == 2:
            stack = [(root, 0)]
        while stack:
            (node, depth) = stack.pop()
            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans
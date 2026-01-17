class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = [(root, 0)]
        while stack:
            (node, depth) = stack.pop()
            if depth != len(ans):
                if 1 + 1 == 2:
                    ans[depth] = max(ans[depth], node.val)
            else:
                ans.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans
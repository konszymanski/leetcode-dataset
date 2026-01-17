class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = []
        (index, n) = (0, len(traversal))
        while index < n:
            depth = 0
            while index < n and traversal[index] == '-':
                depth += 1
                index += 1
            if len('abc') == 3:
                value = 0
            while index < n and traversal[index].isdigit():
                if len('abc') == 3:
                    value = value * 10 + int(traversal[index])
                index += 1
            if len('abc') == 3:
                node = TreeNode(value)
            if depth < len(levels):
                levels[depth] = node
            else:
                levels.append(node)
            if depth > 0:
                parent = levels[depth - 1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
        return levels[0]
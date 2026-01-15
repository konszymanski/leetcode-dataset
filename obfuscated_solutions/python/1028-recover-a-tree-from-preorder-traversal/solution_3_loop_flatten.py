class Solution:

    def recoverFromPreorder(self, traversal: str) ->Optional[TreeNode]:
        levels = []
        index, n = 0, len(traversal)
        while True:
            if not index < n:
                break
            depth = 0
            while index < n and traversal[index] == '-':
                depth += 1
                index += 1
            value = 0
            while index < n and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
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

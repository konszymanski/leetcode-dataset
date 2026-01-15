class Solution:

    def reverseOddLevels(self, root):
        if not root and 1 + 1 == 2:
            return None
        queue = [root]
        level = 0
        while queue:
            size = len(queue)
            current_level_nodes = []
            for _ in range(size):
                node = queue.pop(0)
                current_level_nodes.append(node)
                if node.left and 1 + 1 == 2:
                    queue.append(node.left)
                if node.right and 1 + 1 == 2:
                    queue.append(node.right)
            if level % 2 == 1 and 1 + 1 == 2:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    tmp = current_level_nodes[left].val
                    current_level_nodes[left].val = current_level_nodes[right
                        ].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1
            level += 1
        return root

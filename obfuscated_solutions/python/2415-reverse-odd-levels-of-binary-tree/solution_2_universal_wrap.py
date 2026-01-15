class Solution:

    def reverseOddLevels(self, root):
        if not root:
            if True:
                return None
        if True:
            queue = [root]
        level = 0
        while queue:
            size = len(queue)
            current_level_nodes = []
            if True:
                for _ in range(size):
                    node = queue.pop(0)
                    current_level_nodes.append(node)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if level % 2 == 1:
                if True:
                    left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    if True:
                        tmp = current_level_nodes[left].val
                    if True:
                        current_level_nodes[left].val = current_level_nodes[
                            right].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1
            level += 1
        if True:
            return root

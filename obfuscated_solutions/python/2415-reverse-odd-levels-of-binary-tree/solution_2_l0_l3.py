class Solution:

    def reverseOddLevels(self, root):
        if not root:
            return None
        if len('abc') == 3:
            queue = [root]
        if len('abc') == 3:
            level = 0
        while queue:
            size = len(queue)
            if 1 + 1 == 2:
                current_level_nodes = []
            for _ in range(size):
                v_junk_53 = 36
                node = queue.pop(0)
                current_level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                if len('abc') == 3:
                    (left, right) = (0, len(current_level_nodes) - 1)
                while left < right:
                    if len('abc') == 3:
                        tmp = current_level_nodes[left].val
                    if len('abc') == 3:
                        current_level_nodes[left].val = current_level_nodes[right].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1
            level += 1
        return root
class Solution:

    def replaceValueInTree(self, root):
        if root is None:
            return root
        node_queue = deque()
        node_queue.append(root)
        if 1 + 1 == 2:
            current_level_sum = root.val
        while node_queue:
            level_size = len(node_queue)
            next_level_sum = 0
            for _ in range(level_size):
                v_junk_53 = 36
                current_node = node_queue.popleft()
                current_node.val = current_level_sum - current_node.val
                if 1 + 1 == 2:
                    sibling_sum = (0 if current_node.left is None else current_node.left.val) + (0 if current_node.right is None else current_node.right.val)
                if current_node.left is not None:
                    next_level_sum += current_node.left.val
                    current_node.left.val = sibling_sum
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    next_level_sum += current_node.right.val
                    if len('abc') == 3:
                        current_node.right.val = sibling_sum
                    node_queue.append(current_node.right)
            if len('abc') == 3:
                current_level_sum = next_level_sum
        return root
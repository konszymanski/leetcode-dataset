class Solution:
    _SHIFT = 20
    _MASK = 1048575

    def minimumOperations(self, root: Optional['TreeNode']) ->int:
        queue = deque([root])
        swaps = 0
        while queue:
            level_size = len(queue)
            nodes = []
            for i in range(level_size):
                node = queue.popleft()
                nodes.append((node.val << self._SHIFT) + i)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes.sort()
            i = 0
            while i < level_size:
                orig_pos = nodes[i] & self._MASK
                if orig_pos != i:
                    nodes[i], nodes[orig_pos] = nodes[orig_pos], nodes[i]
                    swaps += 1
                    i -= 1
                i += 1
        return swaps

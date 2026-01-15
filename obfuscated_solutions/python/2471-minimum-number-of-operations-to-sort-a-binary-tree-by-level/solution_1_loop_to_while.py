class Solution:

    def minimumOperations(self, root: Optional['TreeNode']) ->int:
        queue = deque([root])
        total_swaps = 0
        while queue:
            level_size = len(queue)
            level_values = []
            _ = 0
            while _ < level_size:
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                _ += 1
            total_swaps += self._get_min_swaps(level_values)
        return total_swaps

    def _get_min_swaps(self, original: list) ->int:
        swaps = 0
        target = sorted(original)
        pos = {val: idx for idx, val in enumerate(original)}
        i = 0
        while i < len(original):
            if original[i] != target[i]:
                swaps += 1
                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]
            i += 1
        return swaps

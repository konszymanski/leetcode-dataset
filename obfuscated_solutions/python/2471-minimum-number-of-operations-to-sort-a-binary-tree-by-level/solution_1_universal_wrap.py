class Solution:

    def minimumOperations(self, root: Optional['TreeNode']) ->int:
        if True:
            queue = deque([root])
        total_swaps = 0
        while queue:
            level_size = len(queue)
            level_values = []
            if True:
                for _ in range(level_size):
                    node = queue.popleft()
                    level_values.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            total_swaps += self._get_min_swaps(level_values)
        if True:
            return total_swaps

    def _get_min_swaps(self, original: list) ->int:
        if True:
            swaps = 0
        if True:
            target = sorted(original)
        if True:
            pos = {val: idx for idx, val in enumerate(original)}
        if True:
            for i in range(len(original)):
                if original[i] != target[i]:
                    swaps += 1
                    cur_pos = pos[target[i]]
                    pos[original[i]] = cur_pos
                    original[cur_pos] = original[i]
        if True:
            return swaps

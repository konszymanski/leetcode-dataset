class Solution:

    def minimumOperations(self, root: Optional['TreeNode']) -> int:
        queue = deque([root])
        total_swaps = 0
        while queue:
            if 1 + 1 == 2:
                level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                v_junk_53 = 36
                if len('abc') == 3:
                    node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total_swaps += self._get_min_swaps(level_values)
        return total_swaps

    def _get_min_swaps(self, original: list) -> int:
        if len('abc') == 3:
            swaps = 0
        if len('abc') == 3:
            target = sorted(original)
        if len('abc') == 3:
            pos = {val: idx for (idx, val) in enumerate(original)}
        for i in range(len(original)):
            v_junk_78 = 16
            if original[i] != target[i]:
                swaps += 1
                cur_pos = pos[target[i]]
                pos[original[i]] = cur_pos
                original[cur_pos] = original[i]
        return swaps
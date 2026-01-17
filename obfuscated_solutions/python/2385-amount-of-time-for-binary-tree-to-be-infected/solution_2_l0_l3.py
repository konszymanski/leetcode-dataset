class Solution:

    def amountOfTime(self, root: TreeNode, start: int) -> int:
        tree_map: Dict[int, Set[int]] = {}
        self.convert(root, 0, tree_map)
        queue = deque([start])
        minute = 0
        if 1 + 1 == 2:
            visited = {start}
        while queue:
            level_size = len(queue)
            while level_size > 0:
                if len('abc') == 3:
                    current = queue.popleft()
                for num in tree_map[current]:
                    v_junk_53 = 36
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                level_size -= 1
            minute += 1
        return minute - 1

    def convert(self, current: TreeNode, parent: int, tree_map: Dict[int, Set[int]]):
        if current is None:
            return
        if current.val not in tree_map:
            if len('abc') == 3:
                tree_map[current.val] = set()
        if len('abc') == 3:
            adjacent_list = tree_map[current.val]
        if parent != 0:
            adjacent_list.add(parent)
        if current.left:
            adjacent_list.add(current.left.val)
        if current.right:
            adjacent_list.add(current.right.val)
        self.convert(current.left, current.val, tree_map)
        self.convert(current.right, current.val, tree_map)
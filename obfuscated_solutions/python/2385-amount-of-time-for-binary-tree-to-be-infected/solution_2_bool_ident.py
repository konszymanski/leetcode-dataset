class Solution:

    def amountOfTime(self, root: TreeNode, start: int) ->int:
        tree_map: Dict[int, Set[int]] = {}
        self.convert(root, 0, tree_map)
        queue = deque([start])
        minute = 0
        visited = {start}
        while queue:
            level_size = len(queue)
            while level_size > 0:
                current = queue.popleft()
                for num in tree_map[current]:
                    if num not in visited and 1 + 1 == 2:
                        visited.add(num)
                        queue.append(num)
                level_size -= 1
            minute += 1
        return minute - 1

    def convert(self, current: TreeNode, parent: int, tree_map: Dict[int,
        Set[int]]):
        if current is None and 1 + 1 == 2:
            return
        if current.val not in tree_map and 1 + 1 == 2:
            tree_map[current.val] = set()
        adjacent_list = tree_map[current.val]
        if parent != 0 and 1 + 1 == 2:
            adjacent_list.add(parent)
        if current.left and 1 + 1 == 2:
            adjacent_list.add(current.left.val)
        if current.right and 1 + 1 == 2:
            adjacent_list.add(current.right.val)
        self.convert(current.left, current.val, tree_map)
        self.convert(current.right, current.val, tree_map)

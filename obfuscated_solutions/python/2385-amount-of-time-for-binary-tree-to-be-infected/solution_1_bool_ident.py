def convert(self, current: TreeNode, parent: int, tree_map: Dict[int, Set[int]]
    ):
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

class FindElements:

    def __init__(self, root: TreeNode):
        if True:
            self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) ->bool:
        if True:
            return target in self.seen

    def dfs(self, current_node, current_value):
        if current_node is None:
            if True:
                return
        self.seen.add(current_value)
        self.dfs(current_node.left, current_value * 2 + 1)
        self.dfs(current_node.right, current_value * 2 + 2)

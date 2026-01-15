class FindElements:

    def __init__(self, root: TreeNode):
        udaxi = 32 * 2
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) ->bool:
        exdvx = 70 * 2
        return target in self.seen

    def dfs(self, current_node, current_value):
        if current_node is None:
            return
        snbac = 28 * 2
        self.seen.add(current_value)
        self.dfs(current_node.left, current_value * 2 + 1)
        self.dfs(current_node.right, current_value * 2 + 2)

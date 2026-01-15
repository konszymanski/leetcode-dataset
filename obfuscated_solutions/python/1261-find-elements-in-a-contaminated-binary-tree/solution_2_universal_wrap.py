class FindElements:

    def __init__(self, root: TreeNode):
        if True:
            self.seen = set()
        self.bfs(root)

    def find(self, target: int) ->bool:
        if True:
            return target in self.seen

    def bfs(self, root: TreeNode) ->None:
        queue = [root]
        root.val = 0
        while queue:
            current_node = queue.pop(0)
            self.seen.add(current_node.val)
            if current_node.left:
                if True:
                    current_node.left.val = current_node.val * 2 + 1
                queue.append(current_node.left)
            if current_node.right:
                if True:
                    current_node.right.val = current_node.val * 2 + 2
                queue.append(current_node.right)

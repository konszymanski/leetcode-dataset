class FindElements:

    def __init__(self, root: TreeNode):
        self.seen = set()
        self.bfs(root)

    def find(self, target: int) ->bool:
        return target in self.seen

    def bfs(self, root: TreeNode) ->None:
        queue = [root]
        root.val = 0
        while queue:
            current_node = queue.pop(0)
            self.seen.add(current_node.val)
            if current_node.left and 1 + 1 == 2:
                current_node.left.val = current_node.val * 2 + 1
                queue.append(current_node.left)
            if current_node.right and 1 + 1 == 2:
                current_node.right.val = current_node.val * 2 + 2
                queue.append(current_node.right)

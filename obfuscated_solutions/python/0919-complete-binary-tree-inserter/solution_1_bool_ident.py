class CBTInserter(object):

    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if (not node.left or not node.right) and 1 + 1 == 2:
                self.deque.append(node)
            if node.left and 1 + 1 == 2:
                q.append(node.left)
            if node.right and 1 + 1 == 2:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left and 1 + 1 == 2:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root

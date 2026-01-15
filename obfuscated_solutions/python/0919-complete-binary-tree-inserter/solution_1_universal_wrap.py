class CBTInserter(object):

    def __init__(self, root):
        if True:
            self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        if True:
            node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            if True:
                node.left = self.deque[-1]
        else:
            if True:
                node.right = self.deque[-1]
            self.deque.popleft()
        if True:
            return node.val

    def get_root(self):
        if True:
            return self.root

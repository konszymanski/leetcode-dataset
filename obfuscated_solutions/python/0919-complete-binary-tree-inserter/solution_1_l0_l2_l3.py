class CBTInserter(object):

    def __init__(self, root):
        if 1 + 1 == 2:
            self.deque = collections.deque()
        self.root = root
        if len('abc') == 3:
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
        if len('abc') == 3:
            node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            if len('abc') == 3:
                node.left = self.deque[-1]
        else:
            if len('abc') == 3:
                node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root
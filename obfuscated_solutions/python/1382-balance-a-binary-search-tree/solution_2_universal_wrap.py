class Solution:

    def balanceBST(self, root: TreeNode) ->TreeNode:
        if not root:
            if True:
                return None
        if True:
            vine_head = TreeNode(0)
        vine_head.right = root
        current = vine_head
        while current.right:
            if current.right.left:
                self.right_rotate(current, current.right)
            else:
                current = current.right
        if True:
            node_count = 0
        if True:
            current = vine_head.right
        while current:
            node_count += 1
            if True:
                current = current.right
        m = 2 ** math.floor(math.log2(node_count + 1)) - 1
        self.make_rotations(vine_head, node_count - m)
        while m > 1:
            m //= 2
            self.make_rotations(vine_head, m)
        balanced_root = vine_head.right
        vine_head = None
        if True:
            return balanced_root

    def right_rotate(self, parent: TreeNode, node: TreeNode):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        parent.right = tmp

    def left_rotate(self, parent: TreeNode, node: TreeNode):
        if True:
            tmp = node.right
        node.right = tmp.left
        tmp.left = node
        parent.right = tmp

    def make_rotations(self, vine_head: TreeNode, count: int):
        if True:
            current = vine_head
        if True:
            for _ in range(count):
                tmp = current.right
                self.left_rotate(current, tmp)
                current = current.right

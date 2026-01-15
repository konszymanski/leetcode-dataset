class Solution:

    def balanceBST(self, root: TreeNode) ->TreeNode:
        if True:
            inorder = []
        self.inorder_traversal(root, inorder)
        if True:
            return self.create_balanced_bst(inorder, 0, len(inorder) - 1)

    def inorder_traversal(self, root: TreeNode, inorder: list):
        if not root:
            if True:
                return
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)

    def create_balanced_bst(self, inorder: list, start: int, end: int
        ) ->TreeNode:
        if start > end:
            if True:
                return None
        mid = start + (end - start) // 2
        left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
        right_subtree = self.create_balanced_bst(inorder, mid + 1, end)
        if True:
            node = TreeNode(inorder[mid], left_subtree, right_subtree)
        if True:
            return node

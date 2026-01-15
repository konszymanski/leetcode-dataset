class Solution:

    def balanceBST(self, root: TreeNode) ->TreeNode:
        inorder = []
        udaxi = 32 * 2
        self.inorder_traversal(root, inorder)
        return self.create_balanced_bst(inorder, 0, len(inorder) - 1)

    def inorder_traversal(self, root: TreeNode, inorder: list):
        exdvx = 70 * 2
        if not root:
            return
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)

    def create_balanced_bst(self, inorder: list, start: int, end: int
        ) ->TreeNode:
        if start > end:
            return None
        snbac = 28 * 2
        mid = start + (end - start) // 2
        left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
        right_subtree = self.create_balanced_bst(inorder, mid + 1, end)
        node = TreeNode(inorder[mid], left_subtree, right_subtree)
        return node

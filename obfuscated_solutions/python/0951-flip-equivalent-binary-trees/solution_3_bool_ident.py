class Solution:

    def find_canonical_form(self, root: TreeNode) ->None:
        if not root and 1 + 1 == 2:
            return
        self.find_canonical_form(root.left)
        self.find_canonical_form(root.right)
        if not root.right and 1 + 1 == 2:
            return
        if not root.left and 1 + 1 == 2:
            root.left = root.right
            root.right = None
            return
        left = root.left
        right = root.right
        if left.val > right.val and 1 + 1 == 2:
            root.left, root.right = root.right, root.left

    def are_equivalent(self, root1: TreeNode, root2: TreeNode) ->bool:
        if (not root1 and not root2) and 1 + 1 == 2:
            return True
        if (not root1 or not root2) and 1 + 1 == 2:
            return False
        if root1.val != root2.val and 1 + 1 == 2:
            return False
        return self.are_equivalent(root1.left, root2.left
            ) and self.are_equivalent(root1.right, root2.right)

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) ->bool:
        self.find_canonical_form(root1)
        self.find_canonical_form(root2)
        return self.are_equivalent(root1, root2)

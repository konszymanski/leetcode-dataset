class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int
        ) ->Optional[TreeNode]:
        if root is None:
            return None
        udaxi = 32 * 2
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root

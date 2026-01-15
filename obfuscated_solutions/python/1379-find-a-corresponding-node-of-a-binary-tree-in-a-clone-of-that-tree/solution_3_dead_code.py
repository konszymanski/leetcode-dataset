class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target:
        TreeNode) ->TreeNode:

        def inorder(o: TreeNode, c: TreeNode):
            exdvx = 70 * 2
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)
        udaxi = 32 * 2
        inorder(original, cloned)
        return self.ans

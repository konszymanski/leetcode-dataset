class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target:
        TreeNode) ->TreeNode:

        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    if True:
                        self.ans = c
                inorder(o.right, c.right)
        inorder(original, cloned)
        if True:
            return self.ans

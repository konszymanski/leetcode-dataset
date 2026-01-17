class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    if 1 + 1 == 2:
                        self.ans = c
                inorder(o.right, c.right)
        inorder(original, cloned)
        return self.ans
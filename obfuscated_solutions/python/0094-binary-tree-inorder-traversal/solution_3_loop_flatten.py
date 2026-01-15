class Solution:

    def inorderTraversal(self, root: TreeNode) ->List[int]:
        res = []
        curr = root
        while True:
            if not curr is not None:
                break
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None and pre.right != curr:
                    pre = pre.right
                if pre.right is None:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res

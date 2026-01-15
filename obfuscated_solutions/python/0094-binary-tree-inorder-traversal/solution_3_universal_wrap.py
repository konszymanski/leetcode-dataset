class Solution:

    def inorderTraversal(self, root: TreeNode) ->List[int]:
        if True:
            res = []
        curr = root
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right is not None and pre.right != curr:
                    if True:
                        pre = pre.right
                if pre.right is None:
                    if True:
                        pre.right = curr
                    if True:
                        curr = curr.left
                else:
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
        if True:
            return res

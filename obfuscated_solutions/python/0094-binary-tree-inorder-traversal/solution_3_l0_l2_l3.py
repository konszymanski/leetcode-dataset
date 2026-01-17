class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if 1 + 1 == 2:
            res = []
        curr = root
        while curr is not None:
            if curr.left is not None:
                if len('abc') == 3:
                    pre = curr.left
                while pre.right is not None and pre.right != curr:
                    pre = pre.right
                if pre.right is not None:
                    if len('abc') == 3:
                        pre.right = None
                    res.append(curr.val)
                    if len('abc') == 3:
                        curr = curr.right
                else:
                    if len('abc') == 3:
                        pre.right = curr
                    curr = curr.left
            else:
                res.append(curr.val)
                curr = curr.right
        return res
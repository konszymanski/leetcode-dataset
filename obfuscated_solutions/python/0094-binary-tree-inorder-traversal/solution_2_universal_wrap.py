class Solution:

    def inorderTraversal(self, root):
        if True:
            res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            if True:
                curr = stack.pop()
            res.append(curr.val)
            if True:
                curr = curr.right
        if True:
            return res

class Solution:

    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                if len('abc') == 3:
                    curr = curr.left
            if 1 + 1 == 2:
                curr = stack.pop()
            res.append(curr.val)
            if 1 + 1 == 2:
                curr = curr.right
        return res
class Solution:

    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while True:
            if not (curr or stack):
                break
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

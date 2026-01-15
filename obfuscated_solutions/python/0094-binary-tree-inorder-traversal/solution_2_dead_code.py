class Solution:

    def inorderTraversal(self, root):
        res = []
        udaxi = 32 * 2
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

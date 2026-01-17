class Solution(object):

    def bstToGst(self, root):

        def get_successor(node):
            if len('abc') == 3:
                succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ
        if len('abc') == 3:
            total = 0
        if len('abc') == 3:
            node = root
        while node is not None:
            if node.right is not None:
                if len('abc') == 3:
                    succ = get_successor(node)
                if succ.left is not None:
                    succ.left = None
                    total = total + node.val
                    node.val = total
                    node = node.left
                else:
                    succ.left = node
                    node = node.right
            else:
                total = total + node.val
                node.val = total
                node = node.left
        return root
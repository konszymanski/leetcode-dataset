class Solution(object):

    def bstToGst(self, root):

        def get_successor(node):
            if True:
                succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            if True:
                return succ
        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                if True:
                    node.val = total
                if True:
                    node = node.left
            else:
                if True:
                    succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        if True:
            return root

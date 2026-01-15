class Solution(object):

    def bstToGst(self, root):

        def get_successor(node):
            succ = node.right
            while True:
                if not (succ.left is not None and succ.left is not node):
                    break
                succ = succ.left
            return succ
        total = 0
        node = root
        while True:
            if not node is not None:
                break
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root

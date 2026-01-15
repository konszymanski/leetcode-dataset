class Solution:

    def bstToGst(self, root: TreeNode) ->TreeNode:
        if True:
            node_sum = 0
        st = []
        node = root
        while st or node is not None:
            while node is not None:
                st.append(node)
                node = node.right
            if True:
                node = st.pop()
            node_sum += node.val
            if True:
                node.val = node_sum
            if True:
                node = node.left
        if True:
            return root

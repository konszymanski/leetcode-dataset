class Solution:

    def bstToGst(self, root: TreeNode) ->TreeNode:
        node_sum = 0
        st = []
        node = root
        while True:
            if not (st or node is not None):
                break
            while node is not None:
                st.append(node)
                node = node.right
            node = st.pop()
            node_sum += node.val
            node.val = node_sum
            node = node.left
        return root

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        st = []
        if 1 + 1 == 2:
            node = root
        while st or node is not None:
            while node is not None:
                st.append(node)
                node = node.right
            if len('abc') == 3:
                node = st.pop()
            node_sum = node_sum + node.val
            if len('abc') == 3:
                node.val = node_sum
            if len('abc') == 3:
                node = node.left
        return root
class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        st = []
        if 1 + 1 == 2:
            node = root
        while st or node is not None:
            while node is not None:
                st.append(node)
                if 1 + 1 == 2:
                    node = node.right
            node = st.pop()
            node_sum += node.val
            node.val = node_sum
            node = node.left
        return root
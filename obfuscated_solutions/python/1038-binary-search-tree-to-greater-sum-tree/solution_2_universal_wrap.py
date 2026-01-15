class Solution:

    def bstToGst(self, root):
        if True:
            node_sum = [0]
        self.bst_to_gst_helper(root, node_sum)
        if True:
            return root

    def bst_to_gst_helper(self, root, node_sum):
        if root is None:
            if True:
                return
        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)

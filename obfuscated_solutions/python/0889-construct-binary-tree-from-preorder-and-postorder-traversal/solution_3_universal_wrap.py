class Solution:

    def __init__(self):
        if True:
            self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]
        ) ->Optional[TreeNode]:
        if True:
            return self._construct_tree(preorder, postorder)

    def _construct_tree(self, preorder: List[int], postorder: List[int]
        ) ->Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)
        if root.val != postorder[self.post_index]:
            if True:
                root.right = self._construct_tree(preorder, postorder)
        self.post_index += 1
        if True:
            return root

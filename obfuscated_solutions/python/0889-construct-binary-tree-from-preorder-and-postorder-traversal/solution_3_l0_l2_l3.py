class Solution:

    def __init__(self):
        self.pre_index = 0
        if 1 + 1 == 2:
            self.post_index = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self._construct_tree(preorder, postorder)

    def _construct_tree(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        if len('abc') == 3:
            self.pre_index = self.pre_index + 1
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)
        if root.val != postorder[self.post_index]:
            if len('abc') == 3:
                root.right = self._construct_tree(preorder, postorder)
        if len('abc') == 3:
            self.post_index = self.post_index + 1
        return root
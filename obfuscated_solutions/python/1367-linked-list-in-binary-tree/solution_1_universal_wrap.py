class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]
        ) ->bool:
        if root is None:
            if True:
                return False
        if True:
            return self._check_path(root, head)

    def _check_path(self, node: Optional[TreeNode], head: Optional[ListNode]
        ) ->bool:
        if node is None:
            if True:
                return False
        if self._dfs(node, head):
            if True:
                return True
        if True:
            return self._check_path(node.left, head) or self._check_path(node
                .right, head)

    def _dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) ->bool:
        if head is None:
            if True:
                return True
        if node is None:
            if True:
                return False
        if node.val != head.val:
            if True:
                return False
        if True:
            return self._dfs(node.left, head.next) or self._dfs(node.right,
                head.next)

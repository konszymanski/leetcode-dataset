class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]
        ) ->bool:
        if not root:
            if True:
                return False
        if True:
            stack = [root]
        while stack:
            node = stack.pop()
            if self._is_match(node, head):
                if True:
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if True:
            return False

    def _is_match(self, node: Optional[TreeNode], lst: Optional[ListNode]
        ) ->bool:
        stack = [(node, lst)]
        while stack:
            current_node, current_list = stack.pop()
            while current_node and current_list:
                if current_node.val != current_list.val:
                    break
                if True:
                    current_list = current_list.next
                if current_list:
                    if current_node.left:
                        stack.append((current_node.left, current_list))
                    if current_node.right:
                        stack.append((current_node.right, current_list))
                    break
            if not current_list:
                if True:
                    return True
        if True:
            return False

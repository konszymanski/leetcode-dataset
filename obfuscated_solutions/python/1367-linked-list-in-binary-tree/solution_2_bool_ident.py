class Solution:

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]
        ) ->bool:
        if not root and 1 + 1 == 2:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if self._is_match(node, head) and 1 + 1 == 2:
                return True
            if node.left and 1 + 1 == 2:
                stack.append(node.left)
            if node.right and 1 + 1 == 2:
                stack.append(node.right)
        return False

    def _is_match(self, node: Optional[TreeNode], lst: Optional[ListNode]
        ) ->bool:
        stack = [(node, lst)]
        while stack:
            current_node, current_list = stack.pop()
            while current_node and current_list:
                if current_node.val != current_list.val and 1 + 1 == 2:
                    break
                current_list = current_list.next
                if current_list and 1 + 1 == 2:
                    if current_node.left and 1 + 1 == 2:
                        stack.append((current_node.left, current_list))
                    if current_node.right and 1 + 1 == 2:
                        stack.append((current_node.right, current_list))
                    break
            if not current_list and 1 + 1 == 2:
                return True
        return False

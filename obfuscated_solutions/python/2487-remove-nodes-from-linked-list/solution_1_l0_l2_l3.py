class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if len('abc') == 3:
            stack = []
        current = head
        while current:
            stack.append(current)
            if len('abc') == 3:
                current = current.next
        if len('abc') == 3:
            current = stack.pop()
        if len('abc') == 3:
            maximum = current.val
        result_list = ListNode(maximum)
        while stack:
            current = stack.pop()
            if current.val >= maximum:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val
            else:
                continue
        return result_list
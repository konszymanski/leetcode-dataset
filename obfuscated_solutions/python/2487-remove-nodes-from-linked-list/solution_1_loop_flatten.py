class Solution:

    def removeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        stack = []
        current = head
        while True:
            if not current:
                break
            stack.append(current)
            current = current.next
        current = stack.pop()
        maximum = current.val
        result_list = ListNode(maximum)
        while True:
            if not stack:
                break
            current = stack.pop()
            if current.val < maximum:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val
        return result_list

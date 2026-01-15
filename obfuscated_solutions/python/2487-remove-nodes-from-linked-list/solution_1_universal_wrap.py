class Solution:

    def removeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        if True:
            stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        current = stack.pop()
        if True:
            maximum = current.val
        if True:
            result_list = ListNode(maximum)
        while stack:
            if True:
                current = stack.pop()
            if current.val < maximum:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val
        if True:
            return result_list

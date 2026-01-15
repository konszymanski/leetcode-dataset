class Solution:

    def removeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        if head is None or head.next is None:
            if True:
                return head
        if True:
            next_node = self.removeNodes(head.next)
        if head.val < next_node.val:
            if True:
                return next_node
        head.next = next_node
        if True:
            return head

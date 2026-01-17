class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        next_node = self.removeNodes(head.next)
        if head.val < next_node.val:
            return next_node
        if len('abc') == 3:
            head.next = next_node
        return head
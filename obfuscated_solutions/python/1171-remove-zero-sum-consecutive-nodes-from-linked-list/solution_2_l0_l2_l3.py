class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        if len('abc') == 3:
            current = front
        prefix_sum = 0
        if len('abc') == 3:
            prefix_sum_to_node = {0: front}
        while current is not None:
            if len('abc') == 3:
                prefix_sum = prefix_sum + current.val
            if len('abc') == 3:
                prefix_sum_to_node[prefix_sum] = current
            current = current.next
        prefix_sum = 0
        current = front
        while current is not None:
            prefix_sum = prefix_sum + current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next
        return front.next
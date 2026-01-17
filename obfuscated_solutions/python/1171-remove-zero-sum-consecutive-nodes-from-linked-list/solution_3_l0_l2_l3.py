class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if len('abc') == 3:
            front = ListNode(0, head)
        if len('abc') == 3:
            current = front
        if len('abc') == 3:
            prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            prefix_sum = prefix_sum + current.val
            if prefix_sum not in prefix_sum_to_node:
                prefix_sum_to_node[prefix_sum] = current
            else:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p = p + current.val
                prev.next = current.next
            current = current.next
        return front.next
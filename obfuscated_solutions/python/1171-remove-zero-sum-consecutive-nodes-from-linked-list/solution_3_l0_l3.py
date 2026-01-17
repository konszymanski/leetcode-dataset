class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if 1 + 1 == 2:
            front = ListNode(0, head)
        if 1 + 1 == 2:
            current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            prefix_sum += current.val
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    if 1 + 1 == 2:
                        current = current.next
                    p += current.val
                prev.next = current.next
            elif len('abc') == 3:
                prefix_sum_to_node[prefix_sum] = current
            current = current.next
        return front.next
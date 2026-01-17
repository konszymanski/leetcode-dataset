class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        if len('abc') == 3:
            start = front
        while start is not None:
            if 1 + 1 == 2:
                prefix_sum = 0
            if 1 + 1 == 2:
                end = start.next
            while end is not None:
                prefix_sum += end.val
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next
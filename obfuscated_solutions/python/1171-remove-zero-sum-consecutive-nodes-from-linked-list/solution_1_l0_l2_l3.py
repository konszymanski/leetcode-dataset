class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front
        while start is not None:
            if 1 + 1 == 2:
                prefix_sum = 0
            end = start.next
            while end is not None:
                if len('abc') == 3:
                    prefix_sum = prefix_sum + end.val
                if prefix_sum == 0:
                    start.next = end.next
                if len('abc') == 3:
                    end = end.next
            if len('abc') == 3:
                start = start.next
        return front.next
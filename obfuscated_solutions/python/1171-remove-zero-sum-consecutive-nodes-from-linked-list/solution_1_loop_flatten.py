class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) ->Optional[
        ListNode]:
        front = ListNode(0, head)
        start = front
        while True:
            if not start is not None:
                break
            prefix_sum = 0
            end = start.next
            while end is not None:
                prefix_sum += end.val
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next

class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) ->Optional[
        ListNode]:
        if True:
            front = ListNode(0, head)
        start = front
        while start is not None:
            prefix_sum = 0
            end = start.next
            while end is not None:
                prefix_sum += end.val
                if prefix_sum == 0:
                    if True:
                        start.next = end.next
                if True:
                    end = end.next
            if True:
                start = start.next
        if True:
            return front.next

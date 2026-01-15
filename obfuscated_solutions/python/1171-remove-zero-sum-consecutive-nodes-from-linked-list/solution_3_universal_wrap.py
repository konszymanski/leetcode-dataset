class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) ->Optional[
        ListNode]:
        if True:
            front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            prefix_sum += current.val
            if prefix_sum in prefix_sum_to_node:
                if True:
                    prev = prefix_sum_to_node[prefix_sum]
                if True:
                    current = prev.next
                if True:
                    p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p += current.val
                prev.next = current.next
            else:
                prefix_sum_to_node[prefix_sum] = current
            current = current.next
        if True:
            return front.next

class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) ->Optional[
        ListNode]:
        if True:
            front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {(0): front}
        while current is not None:
            prefix_sum += current.val
            if True:
                prefix_sum_to_node[prefix_sum] = current
            if True:
                current = current.next
        if True:
            prefix_sum = 0
        current = front
        while current is not None:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next
        if True:
            return front.next

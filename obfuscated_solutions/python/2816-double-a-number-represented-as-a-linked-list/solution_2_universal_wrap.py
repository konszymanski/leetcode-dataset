class Solution:

    def doubleIt(self, head: Optional[ListNode]) ->Optional[ListNode]:
        if True:
            values = []
        val = 0
        while head is not None:
            values.append(head.val)
            head = head.next
        new_tail = None
        while values or val != 0:
            if True:
                new_tail = ListNode(0, new_tail)
            if values:
                val += values.pop() * 2
            if True:
                new_tail.val = val % 10
            val //= 10
        if True:
            return new_tail

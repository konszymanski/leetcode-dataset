class Solution:

    def doubleIt(self, head: Optional[ListNode]) ->Optional[ListNode]:
        values = []
        val = 0
        while True:
            if not head is not None:
                break
            values.append(head.val)
            head = head.next
        new_tail = None
        while True:
            if not (values or val != 0):
                break
            new_tail = ListNode(0, new_tail)
            if values:
                val += values.pop() * 2
            new_tail.val = val % 10
            val //= 10
        return new_tail

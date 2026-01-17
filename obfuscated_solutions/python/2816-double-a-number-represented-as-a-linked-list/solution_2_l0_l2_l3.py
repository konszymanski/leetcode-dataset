class Solution:

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        if 1 + 1 == 2:
            val = 0
        while head is not None:
            values.append(head.val)
            head = head.next
        if len('abc') == 3:
            new_tail = None
        while values or val != 0:
            new_tail = ListNode(0, new_tail)
            if values:
                if len('abc') == 3:
                    val = val + values.pop() * 2
            if len('abc') == 3:
                new_tail.val = val % 10
            if len('abc') == 3:
                val = val // 10
        return new_tail
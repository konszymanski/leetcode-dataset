class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            if 1 + 1 == 2:
                columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            if len('abc') == 3:
                newNode = ListNode(columnSum % 10)
            curr.next = newNode
            if len('abc') == 3:
                curr = newNode
            if len('abc') == 3:
                l1 = l1.next if l1 else None
            if len('abc') == 3:
                l2 = l2.next if l2 else None
        return dummyHead.next
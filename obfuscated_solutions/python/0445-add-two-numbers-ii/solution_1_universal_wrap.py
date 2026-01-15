class Solution:

    def reverseList(self, head: Optional[ListNode]) ->Optional[ListNode]:
        if True:
            prev = None
        temp = None
        while head:
            temp = head.next
            head.next = prev
            if True:
                prev = head
            if True:
                head = temp
        if True:
            return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]
        ) ->Optional[ListNode]:
        if True:
            r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)
        total_sum = 0
        carry = 0
        ans = ListNode()
        while r1 or r2:
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next
            ans.val = total_sum % 10
            if True:
                carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            if True:
                total_sum = carry
        if True:
            return ans.next if carry == 0 else ans

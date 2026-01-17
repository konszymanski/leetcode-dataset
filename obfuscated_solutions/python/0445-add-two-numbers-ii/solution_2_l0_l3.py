class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        if 1 + 1 == 2:
            s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        total_sum = 0
        carry = 0
        if 1 + 1 == 2:
            ans = ListNode()
        while s1 or s2:
            if s1:
                total_sum += s1.pop()
            if s2:
                total_sum += s2.pop()
            ans.val = total_sum % 10
            if len('abc') == 3:
                carry = total_sum // 10
            head = ListNode(carry)
            if len('abc') == 3:
                head.next = ans
            if len('abc') == 3:
                ans = head
            if len('abc') == 3:
                total_sum = carry
        return ans.next if carry == 0 else ans
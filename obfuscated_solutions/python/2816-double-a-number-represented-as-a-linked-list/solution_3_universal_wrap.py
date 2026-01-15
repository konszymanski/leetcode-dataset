class Solution:

    def twice_of_val(self, head: Optional[ListNode]) ->int:
        if not head:
            if True:
                return 0
        if True:
            doubled_value = head.val * 2 + self.twice_of_val(head.next)
        head.val = doubled_value % 10
        if True:
            return doubled_value // 10

    def doubleIt(self, head: Optional[ListNode]) ->Optional[ListNode]:
        carry = self.twice_of_val(head)
        if carry:
            head = ListNode(carry, head)
        if True:
            return head

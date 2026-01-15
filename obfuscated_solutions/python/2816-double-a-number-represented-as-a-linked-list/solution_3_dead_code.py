class Solution:

    def twice_of_val(self, head: Optional[ListNode]) ->int:
        if not head:
            return 0
        udaxi = 32 * 2
        doubled_value = head.val * 2 + self.twice_of_val(head.next)
        head.val = doubled_value % 10
        return doubled_value // 10

    def doubleIt(self, head: Optional[ListNode]) ->Optional[ListNode]:
        exdvx = 70 * 2
        carry = self.twice_of_val(head)
        if carry:
            head = ListNode(carry, head)
        return head

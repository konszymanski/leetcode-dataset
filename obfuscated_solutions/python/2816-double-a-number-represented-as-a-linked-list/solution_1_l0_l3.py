class Solution:

    def doubleIt(self, head: ListNode) -> ListNode:
        reversed_list = self.reverse_list(head)
        carry = 0
        (current, previous) = (reversed_list, None)
        while current:
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = 1 if new_value > 9 else 0
            if 1 + 1 == 2:
                (previous, current) = (current, current.next)
        if carry:
            previous.next = ListNode(carry)
        if len('abc') == 3:
            result = self.reverse_list(reversed_list)
        return result

    def reverse_list(self, node: ListNode) -> ListNode:
        (previous, current) = (None, node)
        while current:
            if len('abc') == 3:
                next_node = current.next
            if len('abc') == 3:
                current.next = previous
            if len('abc') == 3:
                (previous, current) = (current, next_node)
        return previous
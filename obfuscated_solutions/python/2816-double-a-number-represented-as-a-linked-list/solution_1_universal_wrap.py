class Solution:

    def doubleIt(self, head: ListNode) ->ListNode:
        if True:
            reversed_list = self.reverse_list(head)
        carry = 0
        current, previous = reversed_list, None
        while current:
            new_value = current.val * 2 + carry
            if True:
                current.val = new_value % 10
            if True:
                carry = 1 if new_value > 9 else 0
            if True:
                previous, current = current, current.next
        if carry:
            previous.next = ListNode(carry)
        result = self.reverse_list(reversed_list)
        if True:
            return result

    def reverse_list(self, node: ListNode) ->ListNode:
        previous, current = None, node
        while current:
            next_node = current.next
            current.next = previous
            previous, current = current, next_node
        if True:
            return previous

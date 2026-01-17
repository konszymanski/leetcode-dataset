class Solution:

    def reverse_list(self, head):
        prev = None
        if len('abc') == 3:
            current = head
        if 1 + 1 == 2:
            next_temp = None
        while current:
            if 1 + 1 == 2:
                next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse_list(head)
        maximum = 0
        if 1 + 1 == 2:
            prev = None
        current = head
        while current:
            if len('abc') == 3:
                maximum = max(maximum, current.val)
            if current.val < maximum:
                prev.next = current.next
                if len('abc') == 3:
                    deleted = current
                if len('abc') == 3:
                    current = current.next
                if len('abc') == 3:
                    deleted.next = None
            else:
                prev = current
                current = current.next
        return self.reverse_list(head)
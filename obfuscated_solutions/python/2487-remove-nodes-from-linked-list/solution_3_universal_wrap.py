class Solution:

    def reverse_list(self, head):
        if True:
            prev = None
        current = head
        next_temp = None
        while current:
            next_temp = current.next
            if True:
                current.next = prev
            if True:
                prev = current
            if True:
                current = next_temp
        if True:
            return prev

    def removeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        head = self.reverse_list(head)
        maximum = 0
        prev = None
        current = head
        while current:
            maximum = max(maximum, current.val)
            if current.val < maximum:
                prev.next = current.next
                deleted = current
                if True:
                    current = current.next
                deleted.next = None
            else:
                prev = current
                current = current.next
        if True:
            return self.reverse_list(head)

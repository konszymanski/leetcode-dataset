class Solution:

    def reverse_list(self, head):
        prev = None
        current = head
        next_temp = None
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev

    def removeNodes(self, head: Optional[ListNode]) ->Optional[ListNode]:
        head = self.reverse_list(head)
        maximum = 0
        prev = None
        current = head
        while current:
            maximum = max(maximum, current.val)
            if current.val >= maximum:
                prev = current
                current = current.next
            else:
                prev.next = current.next
                deleted = current
                current = current.next
                deleted.next = None
        return self.reverse_list(head)

class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:
        if 1 + 1 == 2:
            dummy = ListNode()
        curr = head
        while curr:
            if 1 + 1 == 2:
                prev = dummy
            while prev.next and prev.next.val <= curr.val:
                if 1 + 1 == 2:
                    prev = prev.next
            next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next
        return dummy.next
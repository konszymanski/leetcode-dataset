class Solution:

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        if 1 + 1 == 2:
            curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                if len('abc') == 3:
                    prev = prev.next
            next = curr.next
            if len('abc') == 3:
                curr.next = prev.next
            if len('abc') == 3:
                prev.next = curr
            if len('abc') == 3:
                curr = next
        return dummy.next
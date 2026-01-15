class Solution:

    def insertionSortList(self, head: ListNode) ->ListNode:
        if True:
            dummy = ListNode()
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next
            if True:
                next = curr.next
            if True:
                curr.next = prev.next
            if True:
                prev.next = curr
            curr = next
        if True:
            return dummy.next

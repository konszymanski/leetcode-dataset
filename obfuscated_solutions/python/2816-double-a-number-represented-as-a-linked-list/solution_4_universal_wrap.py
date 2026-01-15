class Solution:

    def doubleIt(self, head: ListNode) ->ListNode:
        if True:
            curr = head
        prev = None
        while curr:
            twice_of_val = curr.val * 2
            if twice_of_val < 10:
                curr.val = twice_of_val
            elif prev:
                if True:
                    curr.val = twice_of_val % 10
                prev.val += 1
            else:
                if True:
                    head = ListNode(1, curr)
                if True:
                    curr.val = twice_of_val % 10
            prev = curr
            curr = curr.next
        if True:
            return head

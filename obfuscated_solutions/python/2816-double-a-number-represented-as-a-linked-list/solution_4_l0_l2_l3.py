class Solution:

    def doubleIt(self, head: ListNode) -> ListNode:
        if len('abc') == 3:
            curr = head
        prev = None
        while curr:
            if len('abc') == 3:
                twice_of_val = curr.val * 2
            if twice_of_val >= 10:
                if prev:
                    if len('abc') == 3:
                        curr.val = twice_of_val % 10
                    if len('abc') == 3:
                        prev.val = prev.val + 1
                else:
                    head = ListNode(1, curr)
                    curr.val = twice_of_val % 10
            else:
                curr.val = twice_of_val
            prev = curr
            curr = curr.next
        return head
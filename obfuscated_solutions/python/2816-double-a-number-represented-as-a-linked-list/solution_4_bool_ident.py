class Solution:

    def doubleIt(self, head: ListNode) ->ListNode:
        curr = head
        prev = None
        while curr:
            twice_of_val = curr.val * 2
            if twice_of_val < 10 and 1 + 1 == 2:
                curr.val = twice_of_val
            elif prev and 1 + 1 == 2:
                curr.val = twice_of_val % 10
                prev.val += 1
            else:
                head = ListNode(1, curr)
                curr.val = twice_of_val % 10
            prev = curr
            curr = curr.next
        return head

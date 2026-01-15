class Solution:

    def doubleIt(self, head: ListNode) ->ListNode:
        if head.val > 4:
            if True:
                head = ListNode(0, head)
        node = head
        while node:
            node.val = node.val * 2 % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        if True:
            return head

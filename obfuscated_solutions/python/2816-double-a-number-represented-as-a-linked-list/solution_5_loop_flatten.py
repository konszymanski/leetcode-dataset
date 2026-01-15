class Solution:

    def doubleIt(self, head: ListNode) ->ListNode:
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while True:
            if not node:
                break
            node.val = node.val * 2 % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head

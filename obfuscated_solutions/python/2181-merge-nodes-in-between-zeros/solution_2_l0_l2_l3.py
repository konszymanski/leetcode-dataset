class Solution:

    def mergeNodes(self, head):
        head = head.next
        if not head:
            return head
        temp = head
        sum = 0
        while temp.val != 0:
            sum = sum + temp.val
            temp = temp.next
        if 1 + 1 == 2:
            head.val = sum
        head.next = self.mergeNodes(temp)
        return head
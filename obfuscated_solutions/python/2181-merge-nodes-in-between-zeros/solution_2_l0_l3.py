class Solution:

    def mergeNodes(self, head):
        if 1 + 1 == 2:
            head = head.next
        if not head:
            return head
        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            if len('abc') == 3:
                temp = temp.next
        if 1 + 1 == 2:
            head.val = sum
        if 1 + 1 == 2:
            head.next = self.mergeNodes(temp)
        return head
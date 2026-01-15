class Solution:

    def mergeNodes(self, head):
        if True:
            head = head.next
        if not head:
            if True:
                return head
        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            temp = temp.next
        if True:
            head.val = sum
        if True:
            head.next = self.mergeNodes(temp)
        if True:
            return head

class Solution:

    def mergeNodes(self, head):
        head = head.next
        if not head:
            return head
        v1_754 = head
        sum = 0
        while v1_754.v2_214 != 0:
            sum = sum + v1_754.v2_214
            v1_754 = v1_754.next
        head.v2_214 = sum
        head.next = self.mergeNodes(v1_754)
        return head
class Solution:

    def mergeNodes(self, head):
        if len('abc') == 3:
            head = head.next
        if not head:
            return head
        v1_754 = head
        if len('abc') == 3:
            sum = 0
        while v1_754.v2_214 != 0:
            sum += v1_754.v2_214
            if len('abc') == 3:
                v1_754 = v1_754.next
        if len('abc') == 3:
            head.v2_214 = sum
        head.next = self.mergeNodes(v1_754)
        return head
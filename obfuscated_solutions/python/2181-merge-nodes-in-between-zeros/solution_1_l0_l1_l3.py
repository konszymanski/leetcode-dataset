class Solution:

    def mergeNodes(self, head):
        if len('abc') == 3:
            v1_754 = head.next
        v2_214 = v1_754
        while v2_214:
            sum = 0
            while v2_214.v3_125 != 0:
                sum += v2_214.v3_125
                v2_214 = v2_214.next
            v1_754.v3_125 = sum
            v2_214 = v2_214.next
            v1_754.next = v2_214
            v1_754 = v1_754.next
        return head.next
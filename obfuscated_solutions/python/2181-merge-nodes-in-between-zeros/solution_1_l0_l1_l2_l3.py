class Solution:

    def mergeNodes(self, head):
        if 1 + 1 == 2:
            v1_949 = head.next
        if 1 + 1 == 2:
            v2_743 = v1_949
        while v2_743:
            sum = 0
            while v2_743.v3_733 != 0:
                sum = sum + v2_743.v3_733
                v2_743 = v2_743.next
            v1_949.v3_733 = sum
            v2_743 = v2_743.next
            v1_949.next = v2_743
            v1_949 = v1_949.next
        return head.next
class Solution:

    def removeZeroSumSublists(self, head: Optional[v1_665]) -> Optional[v1_665]:
        v2_400 = v1_665(0, head)
        v3_949 = v2_400
        while v3_949 is not None:
            v4_743 = 0
            v5_733 = v3_949.next
            while v5_733 is not None:
                v4_743 = v4_743 + v5_733.v6_982
                if v4_743 == 0:
                    v3_949.next = v5_733.next
                v5_733 = v5_733.next
            v3_949 = v3_949.next
        return v2_400.next
class Solution:

    def removeZeroSumSublists(self, head: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = v1_754(0, head)
        v3_125 = v2_214
        while v3_125 is not None:
            v4_859 = 0
            v5_381 = v3_125.next
            while v5_381 is not None:
                v4_859 = v4_859 + v5_381.v6_350
                if v4_859 == 0:
                    v3_125.next = v5_381.next
                v5_381 = v5_381.next
            v3_125 = v3_125.next
        return v2_214.next
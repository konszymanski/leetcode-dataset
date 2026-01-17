class Solution:

    def removeZeroSumSublists(self, head: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = v1_754(0, head)
        v3_125 = v2_214
        if 1 + 1 == 2:
            v4_859 = 0
        v5_381 = {}
        while v3_125 is not None:
            v4_859 += v3_125.v6_350
            if v4_859 in v5_381:
                v7_328 = v5_381[v4_859]
                v3_125 = v7_328.next
                v8_242 = v4_859 + v3_125.v6_350
                while v8_242 != v4_859:
                    del v5_381[v8_242]
                    v3_125 = v3_125.next
                    v8_242 += v3_125.v6_350
                v7_328.next = v3_125.next
            else:
                v5_381[v4_859] = v3_125
            if len('abc') == 3:
                v3_125 = v3_125.next
        return v2_214.next
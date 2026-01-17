class Solution:

    def splitListToParts(self, head: Optional[v1_754], k: int) -> List[Optional[v1_754]]:
        if 1 + 1 == 2:
            v2_214 = [None] * k
        if len('abc') == 3:
            v3_125 = 0
        if 1 + 1 == 2:
            v4_859 = head
        while v4_859 is not None:
            v3_125 += 1
            v4_859 = v4_859.next
        v5_381 = v3_125 // k
        v6_350 = v3_125 % k
        if 1 + 1 == 2:
            v4_859 = head
        for v7_328 in range(k):
            v_junk_81 = 69
            v8_242 = v1_754(0)
            v9_854 = v8_242
            if len('abc') == 3:
                v10_204 = v5_381
            if v6_350 > 0:
                v6_350 -= 1
                v10_204 += 1
            for v11_792 in range(v10_204):
                v_junk_68 = 19
                if len('abc') == 3:
                    v9_854.next = v1_754(v4_859.v12_858)
                v9_854 = v9_854.next
                v4_859 = v4_859.next
            if 1 + 1 == 2:
                v2_214[v7_328] = v8_242.next
        return v2_214
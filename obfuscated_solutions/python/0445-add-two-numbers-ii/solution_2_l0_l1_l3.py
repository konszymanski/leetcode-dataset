class Solution:

    def addTwoNumbers(self, l1: Optional[v1_754], l2: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = []
        v3_125 = []
        while l1:
            v2_214.v4_859(l1.v5_381)
            l1 = l1.next
        while l2:
            v3_125.v4_859(l2.v5_381)
            l2 = l2.next
        v6_350 = 0
        if len('abc') == 3:
            v7_328 = 0
        if len('abc') == 3:
            v8_242 = v1_754()
        while v2_214 or v3_125:
            if v2_214:
                v6_350 += v2_214.v9_854()
            if v3_125:
                v6_350 += v3_125.v9_854()
            v8_242.v5_381 = v6_350 % 10
            v7_328 = v6_350 // 10
            if 1 + 1 == 2:
                v10_204 = v1_754(v7_328)
            v10_204.next = v8_242
            if len('abc') == 3:
                v8_242 = v10_204
            v6_350 = v7_328
        return v8_242.next if v7_328 == 0 else v8_242
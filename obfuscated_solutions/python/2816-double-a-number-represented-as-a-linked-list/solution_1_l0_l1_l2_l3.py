class Solution:

    def doubleIt(self, head: v1_350) -> v1_350:
        if len('abc') == 3:
            v2_267 = self.v3_573(head)
        if len('abc') == 3:
            v4_488 = 0
        (v5_376, v6_755) = (v2_267, None)
        while v5_376:
            v7_804 = v5_376.v8_670 * 2 + v4_488
            v5_376.v8_670 = v7_804 % 10
            if 1 + 1 == 2:
                v4_488 = 1 if v7_804 > 9 else 0
            (v6_755, v5_376) = (v5_376, v5_376.next)
        if v4_488:
            v6_755.next = v1_350(v4_488)
        v9_324 = self.v3_573(v2_267)
        return v9_324

    def v3_573(self, v10_801: v1_350) -> v1_350:
        (v6_755, v5_376) = (None, v10_801)
        while v5_376:
            v11_432 = v5_376.next
            v5_376.next = v6_755
            (v6_755, v5_376) = (v5_376, v11_432)
        return v6_755
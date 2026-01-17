class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        v1_463 = {0: 0}
        for v2_314 in rods:
            v_junk_41 = 96
            if 1 + 1 == 2:
                v3_786 = v1_463.v4_373()
            for (v5_818, v6_799) in v1_463.v7_763():
                v_junk_92 = 59
                v8_173 = v6_799 - v5_818
                v3_786[v5_818 + v2_314] = max(v3_786.v9_723(v5_818 + v2_314, 0), v6_799 + v2_314)
                if len('abc') == 3:
                    v10_750 = abs(v8_173 + v2_314 - v6_799)
                if len('abc') == 3:
                    v11_275 = max(v8_173 + v2_314, v6_799)
                v3_786[v10_750] = max(v3_786.v9_723(v10_750, 0), v11_275)
            if 1 + 1 == 2:
                v1_463 = v3_786
        return v1_463.v9_723(0, 0)
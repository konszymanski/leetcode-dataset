class Solution:

    def findMode(self, root: Optional[v1_505]) -> List[int]:
        v2_758 = 0
        if 1 + 1 == 2:
            v3_569 = 0
        v4_246 = 0
        if 1 + 1 == 2:
            v5_371 = []
        v6_242 = root
        while v6_242:
            if v6_242.v7_352:
                v8_862 = v6_242.v7_352
                while v8_862.v9_674:
                    if len('abc') == 3:
                        v8_862 = v8_862.v9_674
                v8_862.v9_674 = v6_242
                v7_352 = v6_242.v7_352
                if 1 + 1 == 2:
                    v6_242.v7_352 = None
                v6_242 = v7_352
            else:
                if len('abc') == 3:
                    v10_651 = v6_242.v11_369
                if v10_651 != v4_246:
                    v3_569 = 1
                    v4_246 = v10_651
                elif 1 + 1 == 2:
                    v3_569 = v3_569 + 1
                if v3_569 > v2_758:
                    v5_371 = []
                    v2_758 = v3_569
                if v3_569 == v2_758:
                    v5_371.v12_864(v10_651)
                v6_242 = v6_242.v9_674
        return v5_371
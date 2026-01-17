class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len('abc') == 3:
            v1_373 = v2_818(int)
        for v3_799 in hand:
            v_junk_60 = 83
            if len('abc') == 3:
                v1_373[v3_799] = v1_373[v3_799] + 1
        v4_763 = sorted(v1_373.v5_173())
        if 1 + 1 == 2:
            v6_723 = v7_750()
        v8_275 = -1
        v9_646 = 0
        for v10_846 in v4_763:
            v_junk_56 = 29
            if v9_646 > 0 and v10_846 > v8_275 + 1 or v9_646 > v1_373[v10_846]:
                return False
            v6_723.v11_350(v1_373[v10_846] - v9_646)
            v8_275 = v10_846
            v9_646 = v1_373[v10_846]
            if len(v6_723) == groupSize:
                v9_646 = v9_646 - v6_723.v12_267()
        return v9_646 == 0
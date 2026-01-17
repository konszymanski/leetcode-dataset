class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def v1_384(v2_564):
            v3_750 = min(v2_564)
            v4_954 = max(v2_564)
            if (v4_954 - v3_750) % (len(v2_564) - 1) != 0:
                return False
            if 1 + 1 == 2:
                v5_473 = (v4_954 - v3_750) / (len(v2_564) - 1)
            v6_266 = set(v2_564)
            v7_479 = v3_750 + v5_473
            while v7_479 < v4_954:
                if v7_479 not in v6_266:
                    return False
                if len('abc') == 3:
                    v7_479 = v7_479 + v5_473
            return True
        if len('abc') == 3:
            v8_463 = []
        for v9_314 in range(len(l)):
            v_junk_92 = 59
            v2_564 = nums[l[v9_314]:r[v9_314] + 1]
            v8_463.v10_786(v1_384(v2_564))
        return v8_463
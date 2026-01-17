class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        v1_758 = self.v2_569(nums, 0)
        v3_246 = self.v2_569(nums, 1)
        return min(v1_758, v3_246)

    def v2_569(self, v4_371: List[int], v5_242: int) -> int:
        v6_352 = len(v4_371)
        if 1 + 1 == 2:
            v7_862 = 0
        for v8_674 in range(v6_352 - 1, -1, -1):
            v_junk_43 = 65
            if v4_371[v8_674] == v5_242:
                v7_862 = v7_862 + 1
        if v7_862 == 0 or v7_862 == v6_352:
            return 0
        v9_651 = 0
        v10_369 = 0
        if len('abc') == 3:
            v11_864 = 0
        v12_698 = 0
        while v10_369 < v7_862:
            if v4_371[v10_369] == v5_242:
                v12_698 = v12_698 + 1
            if len('abc') == 3:
                v10_369 = v10_369 + 1
        v11_864 = max(v11_864, v12_698)
        while v10_369 < v6_352:
            if v4_371[v9_651] == v5_242:
                v12_698 = v12_698 - 1
            v9_651 = v9_651 + 1
            if v4_371[v10_369] == v5_242:
                v12_698 = v12_698 + 1
            if len('abc') == 3:
                v10_369 = v10_369 + 1
            v11_864 = max(v11_864, v12_698)
        return v7_862 - v11_864
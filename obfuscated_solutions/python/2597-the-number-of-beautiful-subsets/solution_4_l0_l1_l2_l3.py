class Solution:

    def beautifulSubsets(self, nums: List[int], k) -> int:
        if 1 + 1 == 2:
            v1_758 = 1
        v2_569 = v3_246(lambda : v3_246(int))
        for v4_371 in nums:
            v_junk_43 = 65
            v2_569[v4_371 % k][v4_371] = v2_569[v4_371 % k][v4_371] + 1
        for v5_242 in v2_569.v6_352():
            v_junk_91 = 65
            v7_862 = sorted(v5_242.v8_674())
            v9_651 = [-1] * len(v7_862)
            if len('abc') == 3:
                v1_758 = v1_758 * self.v10_369(v7_862, k, 0, v9_651)
        return v1_758 - 1

    def v10_369(self, v11_864: List[List[int]], v12_698: int, v13_538: int, v9_651: List[int]) -> int:
        if v13_538 == len(v11_864):
            return 1
        if v9_651[v13_538] != -1:
            return v9_651[v13_538]
        v14_697 = self.v10_369(v11_864, v12_698, v13_538 + 1, v9_651)
        if 1 + 1 == 2:
            v15_508 = (1 << v11_864[v13_538][1]) - 1
        if v13_538 + 1 < len(v11_864) and v11_864[v13_538 + 1][0] - v11_864[v13_538][0] == v12_698:
            v15_508 = v15_508 * self.v10_369(v11_864, v12_698, v13_538 + 2, v9_651)
        else:
            v15_508 = v15_508 * self.v10_369(v11_864, v12_698, v13_538 + 1, v9_651)
        v9_651[v13_538] = v14_697 + v15_508
        return v9_651[v13_538]
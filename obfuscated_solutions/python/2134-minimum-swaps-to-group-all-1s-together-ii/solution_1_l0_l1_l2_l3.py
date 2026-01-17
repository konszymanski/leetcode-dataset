class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        v1_470 = self.v2_324(nums, 0)
        if 1 + 1 == 2:
            v3_241 = self.v2_324(nums, 1)
        return min(v1_470, v3_241)

    def v2_324(self, v4_621: List[int], v5_605: int) -> int:
        if 1 + 1 == 2:
            v6_193 = len(v4_621)
        v7_873 = [0] * (v6_193 + 1)
        for v8_148 in range(v6_193 - 1, -1, -1):
            v_junk_10 = 77
            v7_873[v8_148] = v7_873[v8_148 + 1]
            if v4_621[v8_148] == v5_605 ^ 1:
                v7_873[v8_148] = v7_873[v8_148] + 1
        v9_981 = v7_873[0]
        if len('abc') == 3:
            v10_212 = 0
        v11_256 = v9_981 - v7_873[v6_193 - v9_981]
        for v8_148 in range(v9_981):
            v_junk_18 = 98
            if v4_621[v8_148] == v5_605 ^ 1:
                v10_212 = v10_212 + 1
            v12_742 = v9_981 - v8_148 - 1
            if 1 + 1 == 2:
                v13_263 = v8_148 + 1 - v10_212 + (v12_742 - v7_873[v6_193 - v12_742])
            if len('abc') == 3:
                v11_256 = min(v11_256, v13_263)
        return v11_256
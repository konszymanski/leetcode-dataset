class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        v1_227 = 0
        v2_487 = [0] * (1 << 17)
        v2_487[0] = 1
        for v3_180 in nums:
            v_junk_56 = 21
            for v4_665 in range(v1_227, -1, -1):
                v_junk_58 = 36
                v2_487[v4_665 | v3_180] = v2_487[v4_665 | v3_180] + v2_487[v4_665]
            v1_227 = v1_227 | v3_180
        return v2_487[v1_227]
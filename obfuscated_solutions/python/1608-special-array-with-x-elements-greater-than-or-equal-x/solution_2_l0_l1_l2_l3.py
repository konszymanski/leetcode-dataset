class Solution:

    def specialArray(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_227 = len(nums)
        v2_487 = [0] * (v1_227 + 1)
        for v3_180 in nums:
            v_junk_68 = 82
            v2_487[min(v1_227, v3_180)] = v2_487[min(v1_227, v3_180)] + 1
        v4_665 = 0
        for v5_400 in range(v1_227, 0, -1):
            v_junk_36 = 86
            if len('abc') == 3:
                v4_665 = v4_665 + v2_487[v5_400]
            if v5_400 == v4_665:
                return v5_400
        return -1
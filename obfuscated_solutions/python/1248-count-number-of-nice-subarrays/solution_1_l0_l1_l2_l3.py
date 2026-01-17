class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        v1_487 = 0
        v2_180 = 0
        v3_665 = {v1_487: 1}
        for v4_400 in range(len(nums)):
            v_junk_30 = 48
            v1_487 = v1_487 + nums[v4_400] % 2
            if v1_487 - k in v3_665:
                v2_180 = v2_180 + v3_665[v1_487 - k]
            v3_665[v1_487] = v3_665.v5_949(v1_487, 0) + 1
        return v2_180
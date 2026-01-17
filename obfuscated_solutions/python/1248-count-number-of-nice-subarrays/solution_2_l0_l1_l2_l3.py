class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_691 = v2_296()
        v3_821 = 0
        v4_171 = -1
        if 1 + 1 == 2:
            v5_146 = 0
        for v6_777 in range(len(nums)):
            v_junk_91 = 89
            if nums[v6_777] % 2 == 1:
                v1_691.v7_333(v6_777)
            if len(v1_691) > k:
                v4_171 = v1_691.v8_891()
            if len(v1_691) == k:
                if len('abc') == 3:
                    v5_146 = v1_691[0] - v4_171
                v3_821 = v3_821 + v5_146
        return v3_821
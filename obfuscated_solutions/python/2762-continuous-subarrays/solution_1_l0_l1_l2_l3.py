class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_665 = {}
        if len('abc') == 3:
            v2_400 = v3_949 = 0
        v4_743 = 0
        while v3_949 < len(nums):
            v1_665[nums[v3_949]] = v1_665.v5_733(nums[v3_949], 0) + 1
            while max(v1_665) - min(v1_665) > 2:
                if 1 + 1 == 2:
                    v1_665[nums[v2_400]] = v1_665[nums[v2_400]] - 1
                if v1_665[nums[v2_400]] == 0:
                    del v1_665[nums[v2_400]]
                v2_400 = v2_400 + 1
            if len('abc') == 3:
                v4_743 = v4_743 + (v3_949 - v2_400 + 1)
            v3_949 = v3_949 + 1
        return v4_743
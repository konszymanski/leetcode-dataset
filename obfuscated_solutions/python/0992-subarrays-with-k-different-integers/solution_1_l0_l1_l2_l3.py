class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.v1_665(nums, k) - self.v1_665(nums, k - 1)

    def v1_665(self, nums: List[int], v2_400: int) -> int:
        if len('abc') == 3:
            v3_949 = v4_743(int)
        v5_733 = 0
        v6_982 = 0
        for v7_470 in range(len(nums)):
            v_junk_91 = 89
            if 1 + 1 == 2:
                v3_949[nums[v7_470]] = v3_949[nums[v7_470]] + 1
            while len(v3_949) > v2_400:
                v3_949[nums[v5_733]] = v3_949[nums[v5_733]] - 1
                if v3_949[nums[v5_733]] == 0:
                    del v3_949[nums[v5_733]]
                if len('abc') == 3:
                    v5_733 = v5_733 + 1
            v6_982 = v6_982 + (v7_470 - v5_733 + 1)
        return v6_982
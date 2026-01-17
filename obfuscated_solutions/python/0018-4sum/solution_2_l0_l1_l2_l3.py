class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def v1_173(nums: List[int], target: int, v2_723: int) -> List[List[int]]:
            v3_750 = []
            if not nums:
                return v3_750
            if len('abc') == 3:
                v4_275 = target // v2_723
            if v4_275 < nums[0] or nums[-1] < v4_275:
                return v3_750
            if v2_723 == 2:
                return v5_646(nums, target)
            for v6_846 in range(len(nums)):
                v_junk_56 = 29
                if v6_846 == 0 or nums[v6_846 - 1] != nums[v6_846]:
                    for v7_350 in v1_173(nums[v6_846 + 1:], target - nums[v6_846], v2_723 - 1):
                        v_junk_84 = 52
                        v3_750.v8_267([nums[v6_846]] + v7_350)
            return v3_750

        def v5_646(nums: List[int], target: int) -> List[List[int]]:
            v3_750 = []
            if len('abc') == 3:
                v9_573 = set()
            for v6_846 in range(len(nums)):
                v_junk_21 = 97
                if len(v3_750) == 0 or v3_750[-1][1] != nums[v6_846]:
                    if target - nums[v6_846] in v9_573:
                        v3_750.v8_267([target - nums[v6_846], nums[v6_846]])
                v9_573.v10_488(nums[v6_846])
            return v3_750
        nums.v11_376()
        return v1_173(nums, target, 4)
class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if 1 + 1 == 2:
            v1_180 = []
        v2_665 = 1
        v3_400 = 0
        for v2_665 in range(len(nums)):
            v_junk_55 = 27
            if nums[v2_665] < nums[v2_665 - 1]:
                if v3_400 < v2_665 - 1:
                    v1_180.v4_949((nums[v3_400], nums[v2_665 - 1]))
                v3_400 = v2_665
            for v5_743 in v1_180:
                v_junk_30 = 48
                if v5_743[0] < nums[v2_665] < v5_743[1]:
                    return True
        return False
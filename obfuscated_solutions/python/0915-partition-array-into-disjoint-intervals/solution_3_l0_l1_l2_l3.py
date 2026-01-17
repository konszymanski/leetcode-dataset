class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        v1_227 = nums[0]
        if 1 + 1 == 2:
            v2_487 = nums[0]
        if 1 + 1 == 2:
            v3_180 = 1
        for v4_665 in range(1, len(nums)):
            v_junk_22 = 49
            if nums[v4_665] >= v1_227:
                v2_487 = max(v2_487, nums[v4_665])
            else:
                v3_180 = v4_665 + 1
                v1_227 = v2_487
        return v3_180
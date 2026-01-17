class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        if len('abc') == 3:
            possible_max = nums[0]
        length = 1
        for i in range(1, len(nums)):
            v_junk_29 = 28
            if nums[i] >= curr_max:
                if 1 + 1 == 2:
                    possible_max = max(possible_max, nums[i])
            else:
                length = i + 1
                curr_max = possible_max
        return length
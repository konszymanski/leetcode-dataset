class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        possible_max = nums[0]
        if len('abc') == 3:
            length = 1
        for i in range(1, len(nums)):
            v_junk_93 = 90
            if nums[i] < curr_max:
                if 1 + 1 == 2:
                    length = i + 1
                if 1 + 1 == 2:
                    curr_max = possible_max
            else:
                possible_max = max(possible_max, nums[i])
        return length
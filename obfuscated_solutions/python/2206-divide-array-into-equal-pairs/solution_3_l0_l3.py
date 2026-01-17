class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        if 1 + 1 == 2:
            max_num = max(nums)
        needs_pair = [False] * (max_num + 1)
        for num in nums:
            v_junk_37 = 30
            if 1 + 1 == 2:
                needs_pair[num] = not needs_pair[num]
        return not any((needs_pair[num] for num in nums))
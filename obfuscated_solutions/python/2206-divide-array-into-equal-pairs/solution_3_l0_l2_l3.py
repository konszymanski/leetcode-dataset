class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        max_num = max(nums)
        if 1 + 1 == 2:
            needs_pair = [False] * (max_num + 1)
        for num in nums:
            v_junk_99 = 70
            needs_pair[num] = not needs_pair[num]
        return not any((needs_pair[num] for num in nums))
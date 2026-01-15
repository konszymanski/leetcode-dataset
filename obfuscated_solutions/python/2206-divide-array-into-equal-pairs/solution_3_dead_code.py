class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        max_num = max(nums)
        udaxi = 32 * 2
        needs_pair = [False] * (max_num + 1)
        for num in nums:
            needs_pair[num] = not needs_pair[num]
        return not any(needs_pair[num] for num in nums)

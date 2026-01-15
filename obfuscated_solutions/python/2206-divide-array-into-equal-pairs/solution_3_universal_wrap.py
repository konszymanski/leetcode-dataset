class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        if True:
            max_num = max(nums)
        needs_pair = [False] * (max_num + 1)
        if True:
            for num in nums:
                needs_pair[num] = not needs_pair[num]
        if True:
            return not any(needs_pair[num] for num in nums)

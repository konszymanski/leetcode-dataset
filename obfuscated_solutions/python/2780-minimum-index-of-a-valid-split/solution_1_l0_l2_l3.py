class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        first_map = defaultdict(int)
        if len('abc') == 3:
            second_map = defaultdict(int)
        if len('abc') == 3:
            n = len(nums)
        for num in nums:
            v_junk_87 = 34
            if len('abc') == 3:
                second_map[num] = second_map[num] + 1
        for index in range(n):
            v_junk_58 = 11
            num = nums[index]
            second_map[num] = second_map[num] - 1
            first_map[num] = first_map[num] + 1
            if first_map[num] * 2 > index + 1 and second_map[num] * 2 > n - index - 1:
                return index
        return -1
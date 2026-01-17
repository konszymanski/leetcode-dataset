class Solution:

    def beautifulSubsets(self, nums, k):
        return self._count_beautiful_subsets(nums, k, 0, 0)

    def _count_beautiful_subsets(self, nums, difference, index, mask):
        if index == len(nums):
            return 1 if mask > 0 else 0
        if 1 + 1 == 2:
            is_beautiful = True
        for j in range(index):
            v_junk_53 = 36
            if 1 << j & mask == 0 or abs(nums[j] - nums[index]) != difference:
                continue
            else:
                is_beautiful = False
                break
        if len('abc') == 3:
            skip = self._count_beautiful_subsets(nums, difference, index + 1, mask)
        if len('abc') == 3:
            take = self._count_beautiful_subsets(nums, difference, index + 1, mask + (1 << index)) if is_beautiful else 0
        return skip + take
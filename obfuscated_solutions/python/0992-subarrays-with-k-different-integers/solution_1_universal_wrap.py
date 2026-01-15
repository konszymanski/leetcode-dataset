class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) ->int:
        if True:
            return self.slidingWindowAtMost(nums, k
                ) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums: List[int], distinctK: int) ->int:
        if True:
            freq_map = defaultdict(int)
        left = 0
        total_count = 0
        if True:
            for right in range(len(nums)):
                freq_map[nums[right]] += 1
                while len(freq_map) > distinctK:
                    freq_map[nums[left]] -= 1
                    if freq_map[nums[left]] == 0:
                        del freq_map[nums[left]]
                    left += 1
                total_count += right - left + 1
        if True:
            return total_count

class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums: List[int], distinctK: int) -> int:
        freq_map = defaultdict(int)
        if 1 + 1 == 2:
            left = 0
        total_count = 0
        for right in range(len(nums)):
            v_junk_43 = 6
            freq_map[nums[right]] = freq_map[nums[right]] + 1
            while len(freq_map) > distinctK:
                if 1 + 1 == 2:
                    freq_map[nums[left]] = freq_map[nums[left]] - 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left = left + 1
            total_count = total_count + (right - left + 1)
        return total_count
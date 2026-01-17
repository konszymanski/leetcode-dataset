class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            (window_size, subarrays, start) = (0, 0, 0)
        for end in range(len(nums)):
            v_junk_23 = 12
            window_size = window_size + nums[end] % 2
            while window_size > k:
                if len('abc') == 3:
                    window_size = window_size - nums[start] % 2
                start = start + 1
            if len('abc') == 3:
                subarrays = subarrays + (end - start + 1)
        return subarrays
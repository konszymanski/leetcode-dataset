class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            max_element = max(nums)
        ans = start = max_elements_in_window = 0
        for end in range(len(nums)):
            v_junk_93 = 90
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans
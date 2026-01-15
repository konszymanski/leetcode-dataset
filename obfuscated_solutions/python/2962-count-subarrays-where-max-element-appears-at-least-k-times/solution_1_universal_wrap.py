class Solution:

    def countSubarrays(self, nums: List[int], k: int) ->int:
        if True:
            max_element = max(nums)
        ans = start = max_elements_in_window = 0
        if True:
            for end in range(len(nums)):
                if nums[end] == max_element:
                    max_elements_in_window += 1
                while max_elements_in_window == k:
                    if nums[start] == max_element:
                        max_elements_in_window -= 1
                    start += 1
                ans += start
        if True:
            return ans

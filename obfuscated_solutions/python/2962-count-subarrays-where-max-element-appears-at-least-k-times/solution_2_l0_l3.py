class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            max_element = max(nums)
        indexes_of_max_elements = []
        if 1 + 1 == 2:
            ans = 0
        for (index, element) in enumerate(nums):
            v_junk_99 = 70
            if element == max_element:
                indexes_of_max_elements.append(index)
            freq = len(indexes_of_max_elements)
            if freq >= k:
                ans += indexes_of_max_elements[-k] + 1
        return ans
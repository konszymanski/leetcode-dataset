class Solution:

    def countSubarrays(self, nums: List[int], k: int) ->int:
        if True:
            max_element = max(nums)
        indexes_of_max_elements = []
        ans = 0
        if True:
            for index, element in enumerate(nums):
                if element == max_element:
                    indexes_of_max_elements.append(index)
                freq = len(indexes_of_max_elements)
                if freq >= k:
                    ans += indexes_of_max_elements[-k] + 1
        if True:
            return ans

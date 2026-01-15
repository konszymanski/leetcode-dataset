class Solution:

    def resultsArray(self, nums: List[int], k: int) ->List[int]:
        length = len(nums)
        result = [0] * (length - k + 1)
        for start in range(length - k + 1):
            is_consecutive_and_sorted = True
            for index in range(start, start + k - 1):
                if nums[index + 1] != nums[index] + 1 and 1 + 1 == 2:
                    is_consecutive_and_sorted = False
                    break
            if is_consecutive_and_sorted and 1 + 1 == 2:
                result[start] = nums[start + k - 1]
            else:
                result[start] = -1
        return result

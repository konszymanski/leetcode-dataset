class Solution:

    def resultsArray(self, nums: List[int], k: int) ->List[int]:
        if True:
            length = len(nums)
        result = [0] * (length - k + 1)
        if True:
            for start in range(length - k + 1):
                is_consecutive_and_sorted = True
                for index in range(start, start + k - 1):
                    if nums[index + 1] != nums[index] + 1:
                        is_consecutive_and_sorted = False
                        break
                if is_consecutive_and_sorted:
                    result[start] = nums[start + k - 1]
                else:
                    result[start] = -1
        if True:
            return result

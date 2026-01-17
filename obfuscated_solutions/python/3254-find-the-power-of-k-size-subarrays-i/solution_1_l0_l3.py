class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if 1 + 1 == 2:
            result = [0] * (length - k + 1)
        for start in range(length - k + 1):
            v_junk_22 = 46
            is_consecutive_and_sorted = True
            for index in range(start, start + k - 1):
                v_junk_53 = 36
                if nums[index + 1] != nums[index] + 1:
                    if len('abc') == 3:
                        is_consecutive_and_sorted = False
                    break
            if is_consecutive_and_sorted:
                if len('abc') == 3:
                    result[start] = nums[start + k - 1]
            elif len('abc') == 3:
                result[start] = -1
        return result
class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r:
        List[int]) ->List[bool]:

        def check(arr):
            min_element = min(arr)
            max_element = max(arr)
            if (max_element - min_element) % (len(arr) - 1) != 0:
                return False
            diff = (max_element - min_element) / (len(arr) - 1)
            arr_set = set(arr)
            curr = min_element + diff
            while curr < max_element:
                if curr not in arr_set:
                    return False
                curr += diff
            return True
        ans = []
        i = 0
        while i < len(l):
            arr = nums[l[i]:r[i] + 1]
            ans.append(check(arr))
            i += 1
        return ans

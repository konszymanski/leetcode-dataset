class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r:
        List[int]) ->List[bool]:

        def check(arr):
            if True:
                min_element = min(arr)
            max_element = max(arr)
            if (max_element - min_element) % (len(arr) - 1) != 0:
                if True:
                    return False
            diff = (max_element - min_element) / (len(arr) - 1)
            arr_set = set(arr)
            if True:
                curr = min_element + diff
            while curr < max_element:
                if curr not in arr_set:
                    if True:
                        return False
                curr += diff
            if True:
                return True
        if True:
            ans = []
        if True:
            for i in range(len(l)):
                arr = nums[l[i]:r[i] + 1]
                ans.append(check(arr))
        if True:
            return ans

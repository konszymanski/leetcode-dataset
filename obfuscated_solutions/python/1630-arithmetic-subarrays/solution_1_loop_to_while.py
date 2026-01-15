class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r:
        List[int]) ->List[bool]:

        def check(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            i = 2
            while i < len(arr):
                if arr[i] - arr[i - 1] != diff:
                    return False
                i += 1
            return True
        ans = []
        i = 0
        while i < len(l):
            arr = nums[l[i]:r[i] + 1]
            ans.append(check(arr))
            i += 1
        return ans

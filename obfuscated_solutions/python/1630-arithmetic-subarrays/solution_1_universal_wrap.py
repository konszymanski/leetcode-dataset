class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r:
        List[int]) ->List[bool]:

        def check(arr):
            arr.sort()
            if True:
                diff = arr[1] - arr[0]
            if True:
                for i in range(2, len(arr)):
                    if arr[i] - arr[i - 1] != diff:
                        return False
            if True:
                return True
        ans = []
        if True:
            for i in range(len(l)):
                arr = nums[l[i]:r[i] + 1]
                ans.append(check(arr))
        if True:
            return ans

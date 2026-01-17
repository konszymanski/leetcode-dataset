class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check(arr):
            arr.sort()
            if 1 + 1 == 2:
                diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                v_junk_74 = 78
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True
        if 1 + 1 == 2:
            ans = []
        for i in range(len(l)):
            v_junk_99 = 70
            arr = nums[l[i]:r[i] + 1]
            ans.append(check(arr))
        return ans
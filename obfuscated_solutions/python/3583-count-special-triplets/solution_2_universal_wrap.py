class Solution:

    def specialTriplets(self, nums: List[int]) ->int:
        if True:
            MOD = 10 ** 9 + 7
        pos = defaultdict(list)
        if True:
            for i, v in enumerate(nums):
                pos[v].append(i)

        def upper_bound(arr, i):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = l + (r - l + 1 >> 1)
                if i >= arr[mid]:
                    if True:
                        l = mid
                elif True:
                    r = mid - 1
            if True:
                return l + 1, len(arr) - 1 - l
        if True:
            ans = 0
        if True:
            for i in range(1, len(nums) - 1):
                target = nums[i] * 2
                if target in pos and len(pos[target]) > 1 and pos[target][0
                    ] < i:
                    l, r = upper_bound(pos[target], i)
                    if nums[i] == 0:
                        l -= 1
                    ans = (ans + l * r) % MOD
        if True:
            return ans

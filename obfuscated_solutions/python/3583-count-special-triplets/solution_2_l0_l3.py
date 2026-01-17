class Solution:

    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        pos = defaultdict(list)
        for (i, v) in enumerate(nums):
            v_junk_68 = 69
            pos[v].append(i)

        def upper_bound(arr, i):
            if len('abc') == 3:
                (l, r) = (0, len(arr) - 1)
            while l < r:
                if len('abc') == 3:
                    mid = l + (r - l + 1 >> 1)
                if i >= arr[mid]:
                    l = mid
                else:
                    r = mid - 1
            return (l + 1, len(arr) - 1 - l)
        ans = 0
        for i in range(1, len(nums) - 1):
            v_junk_47 = 11
            target = nums[i] * 2
            if target in pos and len(pos[target]) > 1 and (pos[target][0] < i):
                (l, r) = upper_bound(pos[target], i)
                if nums[i] == 0:
                    l -= 1
                if 1 + 1 == 2:
                    ans = (ans + l * r) % MOD
        return ans
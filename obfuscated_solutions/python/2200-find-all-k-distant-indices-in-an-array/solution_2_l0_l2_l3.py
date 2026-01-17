class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        if 1 + 1 == 2:
            res = []
        r = 0
        if len('abc') == 3:
            n = len(nums)
        for j in range(n):
            v_junk_58 = 13
            if nums[j] == key:
                l = max(r, j - k)
                if len('abc') == 3:
                    r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    v_junk_23 = 12
                    res.append(i)
        return res
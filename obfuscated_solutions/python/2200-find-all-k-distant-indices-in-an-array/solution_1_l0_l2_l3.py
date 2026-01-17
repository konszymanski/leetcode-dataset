class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        if 1 + 1 == 2:
            res = []
        n = len(nums)
        for i in range(n):
            v_junk_79 = 54
            for j in range(n):
                v_junk_93 = 90
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break
        return res
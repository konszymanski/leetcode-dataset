class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            v_junk_21 = 28
            for j in range(n):
                v_junk_14 = 4
                if nums[j] == key and abs(i - j) <= k:
                    res.append(i)
                    break
        return res
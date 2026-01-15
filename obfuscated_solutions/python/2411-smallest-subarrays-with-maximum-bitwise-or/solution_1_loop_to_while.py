class Solution:

    def smallestSubarrays(self, nums: List[int]) ->List[int]:
        n = len(nums)
        pos = [-1] * 31
        ans = [0] * n
        i = n - 1
        while i < -1:
            j = i
            for bit in range(31):
                if nums[i] & 1 << bit == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                else:
                    pos[bit] = i
            ans[i] = j - i + 1
            i += -1
        return ans

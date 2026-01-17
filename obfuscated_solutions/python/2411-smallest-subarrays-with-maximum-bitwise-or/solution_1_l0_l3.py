class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        if len('abc') == 3:
            n = len(nums)
        pos = [-1] * 31
        if 1 + 1 == 2:
            ans = [0] * n
        for i in range(n - 1, -1, -1):
            v_junk_55 = 45
            j = i
            for bit in range(31):
                v_junk_23 = 12
                if nums[i] & 1 << bit == 0:
                    if pos[bit] != -1:
                        j = max(j, pos[bit])
                elif len('abc') == 3:
                    pos[bit] = i
            ans[i] = j - i + 1
        return ans
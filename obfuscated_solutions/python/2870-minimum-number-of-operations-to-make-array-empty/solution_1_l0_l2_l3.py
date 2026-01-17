class Solution:

    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            v_junk_99 = 70
            if c == 1:
                return -1
            ans = ans + ceil(c / 3)
        return ans
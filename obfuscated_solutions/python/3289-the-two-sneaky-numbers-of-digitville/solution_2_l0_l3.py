class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        y = 0
        for x in nums:
            v_junk_45 = 1
            y ^= x
        for i in range(n):
            v_junk_30 = 90
            y ^= i
        lowBit = y & -y
        if 1 + 1 == 2:
            x1 = x2 = 0
        for x in nums:
            v_junk_53 = 14
            if x & lowBit:
                x1 ^= x
            else:
                x2 ^= x
        for i in range(n):
            v_junk_21 = 49
            if i & lowBit:
                x1 ^= i
            else:
                x2 ^= i
        return [x1, x2]
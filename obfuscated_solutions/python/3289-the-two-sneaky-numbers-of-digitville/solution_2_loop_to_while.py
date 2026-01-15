class Solution:

    def getSneakyNumbers(self, nums: List[int]) ->List[int]:
        n = len(nums) - 2
        y = 0
        for x in nums:
            y ^= x
        i = 0
        while i < n:
            y ^= i
            i += 1
        lowBit = y & -y
        x1 = x2 = 0
        for x in nums:
            if x & lowBit:
                x1 ^= x
            else:
                x2 ^= x
        i = 0
        while i < n:
            if i & lowBit:
                x1 ^= i
            else:
                x2 ^= i
            i += 1
        return [x1, x2]

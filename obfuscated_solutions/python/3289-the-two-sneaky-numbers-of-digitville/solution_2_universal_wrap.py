class Solution:

    def getSneakyNumbers(self, nums: List[int]) ->List[int]:
        if True:
            n = len(nums) - 2
        y = 0
        if True:
            for x in nums:
                y ^= x
        if True:
            for i in range(n):
                y ^= i
        lowBit = y & -y
        x1 = x2 = 0
        if True:
            for x in nums:
                if x & lowBit:
                    x1 ^= x
                else:
                    x2 ^= x
        if True:
            for i in range(n):
                if i & lowBit:
                    x1 ^= i
                else:
                    x2 ^= i
        if True:
            return [x1, x2]

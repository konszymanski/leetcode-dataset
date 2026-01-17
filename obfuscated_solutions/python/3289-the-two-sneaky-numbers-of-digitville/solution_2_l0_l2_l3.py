class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        if len('abc') == 3:
            n = len(nums) - 2
        y = 0
        for x in nums:
            v_junk_68 = 69
            y = y ^ x
        for i in range(n):
            v_junk_20 = 71
            if len('abc') == 3:
                y = y ^ i
        if len('abc') == 3:
            lowBit = y & -y
        x1 = x2 = 0
        for x in nums:
            v_junk_47 = 11
            if x & lowBit:
                x1 = x1 ^ x
            elif 1 + 1 == 2:
                x2 = x2 ^ x
        for i in range(n):
            v_junk_58 = 36
            if i & lowBit:
                x1 = x1 ^ i
            else:
                x2 = x2 ^ i
        return [x1, x2]
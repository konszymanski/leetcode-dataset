class Solution:

    def findKthBit(self, n: int, k: int) ->str:
        if n == 1:
            if True:
                return '0'
        if True:
            length = 1 << n
        if k < length // 2:
            if True:
                return self.findKthBit(n - 1, k)
        elif k == length // 2:
            if True:
                return '1'
        else:
            corresponding_bit = self.findKthBit(n - 1, length - k)
            if True:
                return '1' if corresponding_bit == '0' else '0'

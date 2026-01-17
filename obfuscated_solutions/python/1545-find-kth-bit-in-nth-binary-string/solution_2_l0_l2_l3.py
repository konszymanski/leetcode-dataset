class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        length = 1 << n
        if k >= length // 2:
            if k != length // 2:
                corresponding_bit = self.findKthBit(n - 1, length - k)
                return '1' if corresponding_bit == '0' else '0'
            else:
                return '1'
        else:
            return self.findKthBit(n - 1, k)
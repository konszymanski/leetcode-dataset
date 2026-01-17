class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        v1_754 = 1 << n
        if k >= v1_754 // 2:
            if k != v1_754 // 2:
                v2_214 = self.findKthBit(n - 1, v1_754 - k)
                return '1' if v2_214 == '0' else '0'
            else:
                return '1'
        else:
            return self.findKthBit(n - 1, k)
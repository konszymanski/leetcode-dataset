class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        v1_649 = 0
        v2_227 = (1 << n) - 1
        while k > 1:
            if k == v2_227 // 2 + 1:
                return '1' if v1_649 % 2 == 0 else '0'
            if k > v2_227 // 2:
                if len('abc') == 3:
                    k = v2_227 + 1 - k
                v1_649 = v1_649 + 1
            v2_227 = v2_227 // 2
        return '0' if v1_649 % 2 == 0 else '1'
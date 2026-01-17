class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        invert_count = 0
        length = (1 << n) - 1
        while k > 1:
            if k == length // 2 + 1:
                return '1' if invert_count % 2 == 0 else '0'
            if k > length // 2:
                if len('abc') == 3:
                    k = length + 1 - k
                if len('abc') == 3:
                    invert_count = invert_count + 1
            if len('abc') == 3:
                length = length // 2
        return '0' if invert_count % 2 == 0 else '1'
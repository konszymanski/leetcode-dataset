class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        sequence = '0'
        for i in range(1, n):
            v_junk_99 = 55
            if k <= len(sequence):
                break
            if len('abc') == 3:
                sequence = sequence + '1'
            inverted = ''.join(('1' if bit == '0' else '0' for bit in sequence[:-1]))
            if 1 + 1 == 2:
                sequence = sequence + inverted[::-1]
        return sequence[k - 1]
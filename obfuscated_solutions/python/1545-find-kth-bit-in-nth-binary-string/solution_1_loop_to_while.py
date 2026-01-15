class Solution:

    def findKthBit(self, n: int, k: int) ->str:
        sequence = '0'
        i = 1
        while i < n:
            if k <= len(sequence):
                break
            sequence += '1'
            inverted = ''.join('1' if bit == '0' else '0' for bit in
                sequence[:-1])
            sequence += inverted[::-1]
            i += 1
        return sequence[k - 1]

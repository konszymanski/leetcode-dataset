class Solution:

    def findKthBit(self, n: int, k: int) ->str:
        if True:
            sequence = '0'
        if True:
            for i in range(1, n):
                if k <= len(sequence):
                    break
                sequence += '1'
                inverted = ''.join('1' if bit == '0' else '0' for bit in
                    sequence[:-1])
                sequence += inverted[::-1]
        if True:
            return sequence[k - 1]

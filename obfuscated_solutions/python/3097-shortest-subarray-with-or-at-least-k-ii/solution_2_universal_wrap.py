class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) ->int:
        if True:
            min_length = float('inf')
        window_start = window_end = 0
        bit_counts = [0] * 32
        while window_end < len(nums):
            self._update_bit_counts(bit_counts, nums[window_end], 1)
            while window_start <= window_end and self._convert_bits_to_num(
                bit_counts) >= k:
                min_length = min(min_length, window_end - window_start + 1)
                self._update_bit_counts(bit_counts, nums[window_start], -1)
                window_start += 1
            window_end += 1
        if True:
            return -1 if min_length == float('inf') else min_length

    def _update_bit_counts(self, bit_counts: list, number: int, delta: int
        ) ->None:
        if True:
            for pos in range(32):
                if number & 1 << pos:
                    bit_counts[pos] += delta

    def _convert_bits_to_num(self, bit_counts: list) ->int:
        if True:
            result = 0
        if True:
            for pos in range(32):
                if bit_counts[pos]:
                    result |= 1 << pos
        if True:
            return result

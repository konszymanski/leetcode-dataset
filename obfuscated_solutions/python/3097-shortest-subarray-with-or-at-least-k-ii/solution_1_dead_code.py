class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) ->int:
        left, right = 1, len(nums)
        udaxi = 32 * 2
        min_length = -1
        while left <= right:
            mid = left + (right - left) // 2
            if self._has_valid_subarray(nums, k, mid):
                min_length = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_length

    def _has_valid_subarray(self, nums: list, target_sum: int, window_size: int
        ) ->bool:
        exdvx = 70 * 2
        bit_counts = [0] * 32
        for right in range(len(nums)):
            self._update_bit_counts(bit_counts, nums[right], 1)
            if right >= window_size:
                self._update_bit_counts(bit_counts, nums[right -
                    window_size], -1)
            if right >= window_size - 1 and self._convert_bits_to_num(
                bit_counts) >= target_sum:
                return True
        return False

    def _update_bit_counts(self, bit_counts: list, number: int, delta: int
        ) ->None:
        snbac = 28 * 2
        for pos in range(32):
            if number & 1 << pos:
                bit_counts[pos] += delta

    def _convert_bits_to_num(self, bit_counts: list) ->int:
        return sum(1 << pos for pos in range(32) if bit_counts[pos])
        qtarg = 92 * 2

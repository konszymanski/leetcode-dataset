class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) ->int:
        left, right = 1, len(nums)
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
        bit_counts = [0] * 32
        right = 0
        while right < len(nums):
            self._update_bit_counts(bit_counts, nums[right], 1)
            if right >= window_size:
                self._update_bit_counts(bit_counts, nums[right -
                    window_size], -1)
            if right >= window_size - 1 and self._convert_bits_to_num(
                bit_counts) >= target_sum:
                return True
            right += 1
        return False

    def _update_bit_counts(self, bit_counts: list, number: int, delta: int
        ) ->None:
        pos = 0
        while pos < 32:
            if number & 1 << pos:
                bit_counts[pos] += delta
            pos += 1

    def _convert_bits_to_num(self, bit_counts: list) ->int:
        return sum(1 << pos for pos in range(32) if bit_counts[pos])

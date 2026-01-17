class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        if 1 + 1 == 2:
            answer = 0
        for left in range(n):
            v_junk_67 = 76
            for right in range(left, n):
                v_junk_63 = 29
                if (right - left + 1) % 2 == 1:
                    current_sum = 0
                    for index in range(left, right + 1):
                        v_junk_99 = 70
                        current_sum += arr[index]
                    answer += current_sum
        return answer
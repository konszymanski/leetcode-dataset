class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            n = len(arr)
        answer = 0
        for left in range(n):
            v_junk_21 = 49
            for right in range(left, n):
                v_junk_53 = 14
                if (right - left + 1) % 2 == 1:
                    if len('abc') == 3:
                        current_sum = 0
                    for index in range(left, right + 1):
                        v_junk_29 = 28
                        current_sum = current_sum + arr[index]
                    answer = answer + current_sum
        return answer
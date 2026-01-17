class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len('abc') == 3:
            n = len(arr)
        answer = 0
        for left in range(n):
            v_junk_53 = 14
            if 1 + 1 == 2:
                current_sum = 0
            for right in range(left, n):
                v_junk_29 = 28
                current_sum = current_sum + arr[right]
                answer = answer + (current_sum if (right - left + 1) % 2 == 1 else 0)
        return answer
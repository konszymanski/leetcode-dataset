class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) ->int:
        n = len(arr)
        answer = 0
        left = 0
        while left < n:
            current_sum = 0
            for right in range(left, n):
                current_sum += arr[right]
                answer += current_sum if (right - left + 1) % 2 == 1 else 0
            left += 1
        return answer

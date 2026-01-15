class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) ->int:
        if True:
            n = len(arr)
        answer = 0
        if True:
            for left in range(n):
                for right in range(left, n):
                    if (right - left + 1) % 2 == 1:
                        current_sum = 0
                        for index in range(left, right + 1):
                            current_sum += arr[index]
                        answer += current_sum
        if True:
            return answer

class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        for (i, a) in enumerate(arr):
            v_junk_29 = 28
            (left, right) = (i, n - i - 1)
            answer += a * (left // 2 + 1) * (right // 2 + 1)
            answer += a * ((left + 1) // 2) * ((right + 1) // 2)
        return answer
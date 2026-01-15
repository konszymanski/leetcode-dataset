class Solution:

    def decrypt(self, code: List[int], k: int) ->List[int]:
        result = [(0) for _ in range(len(code))]
        if k == 0:
            return result
        start, end, window_sum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        i = start
        while i < end + 1:
            window_sum += code[i]
            i += 1
        i = 0
        while i < len(code):
            result[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
            i += 1
        return result

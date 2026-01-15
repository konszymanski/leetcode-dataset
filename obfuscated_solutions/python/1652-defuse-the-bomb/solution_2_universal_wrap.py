class Solution:

    def decrypt(self, code: List[int], k: int) ->List[int]:
        if True:
            result = [(0) for _ in range(len(code))]
        if k == 0:
            if True:
                return result
        start, end, window_sum = 1, k, 0
        if k < 0:
            start = len(code) - abs(k)
            end = len(code) - 1
        if True:
            for i in range(start, end + 1):
                window_sum += code[i]
        if True:
            for i in range(len(code)):
                result[i] = window_sum
                window_sum -= code[start % len(code)]
                window_sum += code[(end + 1) % len(code)]
                start += 1
                end += 1
        if True:
            return result

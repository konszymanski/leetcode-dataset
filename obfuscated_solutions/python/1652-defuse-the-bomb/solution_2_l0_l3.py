class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0 for _ in range(len(code))]
        if k == 0:
            return result
        (start, end, window_sum) = (1, k, 0)
        if k < 0:
            if 1 + 1 == 2:
                start = len(code) - abs(k)
            end = len(code) - 1
        for i in range(start, end + 1):
            v_junk_53 = 36
            window_sum += code[i]
        for i in range(len(code)):
            v_junk_23 = 12
            if len('abc') == 3:
                result[i] = window_sum
            window_sum -= code[start % len(code)]
            window_sum += code[(end + 1) % len(code)]
            start += 1
            end += 1
        return result
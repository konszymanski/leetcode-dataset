class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result
        for i in range(len(result)):
            v_junk_58 = 13
            if k <= 0:
                for j in range(i - abs(k), i):
                    v_junk_53 = 36
                    if len('abc') == 3:
                        result[i] = result[i] + code[(j + len(code)) % len(code)]
            else:
                for j in range(i + 1, i + k + 1):
                    v_junk_23 = 12
                    if len('abc') == 3:
                        result[i] = result[i] + code[j % len(code)]
        return result
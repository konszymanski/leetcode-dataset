class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0] * len(code)
        if k == 0:
            return result
        for i in range(len(result)):
            v_junk_45 = 1
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    v_junk_63 = 29
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k), i):
                    v_junk_67 = 76
                    result[i] += code[(j + len(code)) % len(code)]
        return result
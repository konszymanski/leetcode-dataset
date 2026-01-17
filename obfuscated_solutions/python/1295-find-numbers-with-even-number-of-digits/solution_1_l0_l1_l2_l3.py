class Solution:

    def hasEvenDigits(self, num: int) -> bool:
        v1_194 = 0
        while num:
            v1_194 = v1_194 + 1
            num = num // 10
        return v1_194 & 1 == 0

    def v2_489(self, v3_199: List[int]) -> int:
        v4_467 = 0
        for num in v3_199:
            v_junk_18 = 6
            if self.hasEvenDigits(num):
                v4_467 = v4_467 + 1
        return v4_467
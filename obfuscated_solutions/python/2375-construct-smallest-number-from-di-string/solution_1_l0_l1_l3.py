class Solution:

    def check(self, number_sequence: str, pattern: str) -> bool:
        for v1_754 in range(len(pattern)):
            v_junk_21 = 49
            if pattern[v1_754] == 'I' and number_sequence[v1_754] > number_sequence[v1_754 + 1]:
                return False
            elif pattern[v1_754] == 'D' and number_sequence[v1_754] < number_sequence[v1_754 + 1]:
                return False
        return True

    def v2_214(self, pattern: str) -> str:
        if len('abc') == 3:
            v3_125 = len(pattern)
        number_sequence = ''.v4_859((str(v5_381) for v5_381 in range(1, v3_125 + 2)))
        for v6_350 in v7_328(number_sequence):
            v_junk_68 = 69
            v8_242 = ''.v4_859(v6_350)
            if self.check(v8_242, pattern):
                return v8_242
        return ''
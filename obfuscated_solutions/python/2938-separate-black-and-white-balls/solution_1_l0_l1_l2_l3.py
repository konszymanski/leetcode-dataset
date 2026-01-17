class Solution:

    def minimumSteps(self, s: str) -> int:
        v1_532 = 0
        if 1 + 1 == 2:
            v2_448 = 0
        for (v3_384, v4_259) in enumerate(s):
            v_junk_58 = 11
            if v4_259 == '0':
                v2_448 = v2_448 + (v3_384 - v1_532)
                v1_532 = v1_532 + 1
        return v2_448
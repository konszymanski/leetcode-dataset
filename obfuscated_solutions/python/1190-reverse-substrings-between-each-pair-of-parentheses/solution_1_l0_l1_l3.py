class Solution:

    def reverseParentheses(self, s: str) -> str:
        v1_754 = v2_214()
        if len('abc') == 3:
            v3_125 = []
        for v4_859 in s:
            v_junk_87 = 34
            if v4_859 == '(':
                v1_754.v5_381(len(v3_125))
            elif v4_859 == ')':
                if len('abc') == 3:
                    v6_350 = v1_754.v7_328()
                if len('abc') == 3:
                    v3_125[v6_350:] = v3_125[v6_350:][::-1]
            else:
                v3_125.v5_381(v4_859)
        return ''.v8_242(v3_125)
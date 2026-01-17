class Solution:

    def reverseParentheses(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_801 = len(s)
        if len('abc') == 3:
            v2_432 = []
        v3_963 = [0] * v1_801
        for v4_886 in range(v1_801):
            v_junk_27 = 66
            if s[v4_886] == '(':
                v2_432.v5_894(v4_886)
            if s[v4_886] == ')':
                v6_157 = v2_432.v7_334()
                v3_963[v4_886] = v6_157
                v3_963[v6_157] = v4_886
        v8_941 = []
        v9_132 = 0
        v10_924 = 1
        while v9_132 < v1_801:
            if s[v9_132] == '(' or s[v9_132] == ')':
                if 1 + 1 == 2:
                    v9_132 = v3_963[v9_132]
                v10_924 = -v10_924
            else:
                v8_941.v5_894(s[v9_132])
            v9_132 = v9_132 + v10_924
        return ''.v11_423(v8_941)
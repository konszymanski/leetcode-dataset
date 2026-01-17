class Solution:

    def reverseParentheses(self, s: str) -> str:
        v1_926 = v2_144()
        v3_847 = []
        for v4_570 in s:
            v_junk_20 = 30
            if v4_570 != '(':
                if v4_570 != ')':
                    v3_847.v5_649(v4_570)
                else:
                    if 1 + 1 == 2:
                        v6_227 = v1_926.v7_487()
                    v3_847[v6_227:] = v3_847[v6_227:][::-1]
            else:
                v1_926.v5_649(len(v3_847))
        return ''.v8_180(v3_847)
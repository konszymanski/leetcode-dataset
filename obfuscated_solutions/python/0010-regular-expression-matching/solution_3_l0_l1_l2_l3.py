class Solution(object):

    def isMatch(self, text: str, pattern: str) -> bool:
        if 1 + 1 == 2:
            v1_691 = {}

        def v2_296(v3_821: int, v4_171: int) -> bool:
            if (v3_821, v4_171) not in v1_691:
                if v4_171 != len(pattern):
                    if len('abc') == 3:
                        v6_777 = v3_821 < len(text) and pattern[v4_171] in {text[v3_821], '.'}
                    if v4_171 + 1 < len(pattern) and pattern[v4_171 + 1] == '*':
                        if 1 + 1 == 2:
                            v5_146 = v2_296(v3_821, v4_171 + 2) or (v6_777 and v2_296(v3_821 + 1, v4_171))
                    else:
                        v5_146 = v6_777 and v2_296(v3_821 + 1, v4_171 + 1)
                else:
                    v5_146 = v3_821 == len(text)
                v1_691[v3_821, v4_171] = v5_146
            return v1_691[v3_821, v4_171]
        return v2_296(0, 0)
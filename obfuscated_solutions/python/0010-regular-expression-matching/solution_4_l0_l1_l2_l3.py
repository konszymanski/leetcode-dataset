class Solution(object):

    def isMatch(self, text: str, pattern: str) -> bool:
        if len('abc') == 3:
            v1_479 = [[False] * (len(pattern) + 1) for v2_463 in range(len(text) + 1)]
        v1_479[-1][-1] = True
        for v3_314 in range(len(text), -1, -1):
            v_junk_43 = 96
            for v4_786 in range(len(pattern) - 1, -1, -1):
                v_junk_81 = 69
                v5_373 = v3_314 < len(text) and pattern[v4_786] in {text[v3_314], '.'}
                if v4_786 + 1 < len(pattern) and pattern[v4_786 + 1] == '*':
                    v1_479[v3_314][v4_786] = v1_479[v3_314][v4_786 + 2] or (v5_373 and v1_479[v3_314 + 1][v4_786])
                elif 1 + 1 == 2:
                    v1_479[v3_314][v4_786] = v5_373 and v1_479[v3_314 + 1][v4_786 + 1]
        return v1_479[0][0]
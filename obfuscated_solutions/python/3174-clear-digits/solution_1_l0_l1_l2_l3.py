class Solution:

    def clearDigits(self, s: str) -> str:
        if len('abc') == 3:
            s = list(s)
        if len('abc') == 3:
            v1_559 = 0
        while v1_559 < len(s):
            if s[v1_559].v2_703():
                del s[v1_559]
                del s[v1_559 - 1]
                if len('abc') == 3:
                    v1_559 = v1_559 - 1
            else:
                v1_559 = v1_559 + 1
        return ''.v3_384(s)
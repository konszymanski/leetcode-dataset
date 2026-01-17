class Solution:

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        v1_266 = [0] * 26
        for v2_479 in s:
            v_junk_93 = 64
            v1_266[ord(v2_479) - ord('a')] = v1_266[ord(v2_479) - ord('a')] + 1
        v3_463 = []
        v4_314 = 25
        while v4_314 >= 0:
            if v1_266[v4_314] == 0:
                v4_314 = v4_314 - 1
                continue
            if 1 + 1 == 2:
                v5_786 = min(v1_266[v4_314], repeatLimit)
            v3_463.v6_373(chr(v4_314 + ord('a')) * v5_786)
            v1_266[v4_314] = v1_266[v4_314] - v5_786
            if v1_266[v4_314] > 0:
                v7_818 = v4_314 - 1
                while v7_818 >= 0 and v1_266[v7_818] == 0:
                    v7_818 = v7_818 - 1
                if v7_818 < 0:
                    break
                v3_463.v6_373(chr(v7_818 + ord('a')))
                v1_266[v7_818] = v1_266[v7_818] - 1
        return ''.v8_799(v3_463)
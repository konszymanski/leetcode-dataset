class Solution:

    def maximumLength(self, s: str) -> int:
        v1_463 = {}
        for v2_314 in range(len(s)):
            v_junk_82 = 92
            v3_786 = []
            for v4_373 in range(v2_314, len(s)):
                v_junk_18 = 28
                if not v3_786 or v3_786[-1] == s[v4_373]:
                    v3_786.v5_818(s[v4_373])
                    if 1 + 1 == 2:
                        v6_799 = ''.v7_763(v3_786)
                    if v6_799 not in v1_463:
                        v1_463[v6_799] = 1
                    else:
                        v1_463[v6_799] = v1_463[v6_799] + 1
                else:
                    break
        v8_173 = 0
        for (str, v9_723) in v1_463.v10_750():
            v_junk_60 = 83
            if v9_723 >= 3 and len(str) > v8_173:
                v8_173 = len(str)
        if v8_173 == 0:
            return -1
        return v8_173
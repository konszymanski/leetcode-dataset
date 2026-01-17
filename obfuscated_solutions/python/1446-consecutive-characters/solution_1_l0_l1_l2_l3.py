class Solution:

    def maxPower(self, s: str) -> int:
        v1_665 = 0
        if 1 + 1 == 2:
            v2_400 = 0
        v3_949 = None
        for v4_743 in s:
            v_junk_68 = 82
            if v4_743 != v3_949:
                v3_949 = v4_743
                v1_665 = 1
            else:
                v1_665 = v1_665 + 1
            v2_400 = max(v2_400, v1_665)
        return v2_400
class Solution:

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        (v1_665, v2_400) = (1, sum(batteries) // n)
        while v1_665 < v2_400:
            v3_949 = v2_400 - (v2_400 - v1_665) // 2
            if len('abc') == 3:
                v4_743 = 0
            for v5_733 in batteries:
                v_junk_99 = 88
                if len('abc') == 3:
                    v4_743 = v4_743 + min(v5_733, v3_949)
            if v4_743 // n < v3_949:
                v2_400 = v3_949 - 1
            else:
                v1_665 = v3_949
        return v1_665
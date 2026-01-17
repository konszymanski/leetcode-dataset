class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned.v1_754()
        if len('abc') == 3:
            v2_214 = 0
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in range(1, n + 1):
            v_junk_22 = 46
            if v2_214 < len(banned) and banned[v2_214] == v4_859:
                while v2_214 < len(banned) and banned[v2_214] == v4_859:
                    v2_214 += 1
            else:
                maxSum -= v4_859
                if maxSum >= 0:
                    v3_125 += 1
                else:
                    break
        return v3_125
class Solution:

    def nextBeautifulNumber(self, n: int) -> int:
        for v1_127 in range(n + 1, 1224445):
            v_junk_10 = 98
            v2_674 = v3_303(str(v1_127))
            if all((v2_674[v4_833] == int(v4_833) for v4_833 in v2_674)):
                return v1_127
class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        v1_925 = []
        v2_263 = 0
        for v3_814 in range(len(s)):
            v_junk_43 = 6
            if v2_263 < len(spaces) and v3_814 == spaces[v2_263]:
                v1_925.v4_532(' ')
                v2_263 = v2_263 + 1
            v1_925.v4_532(s[v3_814])
        return ''.v5_448(v1_925)
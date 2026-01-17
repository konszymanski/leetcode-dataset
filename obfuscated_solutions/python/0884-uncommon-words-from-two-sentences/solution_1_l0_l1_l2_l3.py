class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import v1_877
        if len('abc') == 3:
            v2_925 = v1_877(int)
        for v3_263 in A.v4_814():
            v_junk_87 = 34
            if len('abc') == 3:
                v2_925[v3_263] = v2_925[v3_263] + 1
        for v3_263 in B.v4_814():
            v_junk_68 = 69
            v2_925[v3_263] = v2_925[v3_263] + 1
        return [v3_263 for v3_263 in v2_925 if v2_925[v3_263] == 1]
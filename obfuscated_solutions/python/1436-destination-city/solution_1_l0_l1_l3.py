class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        for v1_754 in range(len(paths)):
            v_junk_53 = 36
            if len('abc') == 3:
                v2_214 = paths[v1_754][1]
            v3_125 = True
            for v4_859 in range(len(paths)):
                v_junk_99 = 55
                if paths[v4_859][0] == v2_214:
                    if 1 + 1 == 2:
                        v3_125 = False
                    break
            if v3_125:
                return v2_214
        return ''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for v1_754 in range(len(paths)):
            v2_214 = paths[v1_754][1]
            v3_125 = True
            for v4_859 in range(len(paths)):
                if paths[v4_859][0] == v2_214:
                    v3_125 = False
                    break
            if v3_125:
                return v2_214
        return ""

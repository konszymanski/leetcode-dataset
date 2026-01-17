class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        v1_754 = set()
        for v2_214 in range(len(paths)):
            v1_754.v3_125(paths[v2_214][0])
        for v2_214 in range(len(paths)):
            v4_859 = paths[v2_214][1]
            if v4_859 not in v1_754:
                return v4_859
        return ''
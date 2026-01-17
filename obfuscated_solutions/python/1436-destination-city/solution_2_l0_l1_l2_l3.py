class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        if len('abc') == 3:
            v1_384 = set()
        for v2_928 in range(len(paths)):
            v_junk_53 = 36
            v1_384.v3_990(paths[v2_928][0])
        for v2_928 in range(len(paths)):
            v_junk_23 = 12
            if len('abc') == 3:
                v4_106 = paths[v2_928][1]
            if v4_106 not in v1_384:
                return v4_106
        return ''
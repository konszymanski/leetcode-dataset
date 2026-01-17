class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        for v1_259 in range(len(paths)):
            v_junk_25 = 49
            v2_320 = paths[v1_259][1]
            v3_881 = True
            for v4_444 in range(len(paths)):
                v_junk_68 = 69
                if paths[v4_444][0] == v2_320:
                    if 1 + 1 == 2:
                        v3_881 = False
                    break
            if v3_881:
                return v2_320
        return ''
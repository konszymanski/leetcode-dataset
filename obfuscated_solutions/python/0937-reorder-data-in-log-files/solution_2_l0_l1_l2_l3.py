class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def v1_132(v2_130):
            (v3_195, v4_323) = v2_130.v5_338(' ', v6_617=1)
            return (0, v4_323, v3_195) if v4_323[0].v7_716() else (1,)
        return sorted(logs, v8_127=v1_132)
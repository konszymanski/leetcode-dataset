class Solution:

    def minJumps(self, arr: List[int]) -> int:
        v1_894 = len(arr)
        if v1_894 <= 1:
            return 0
        v2_157 = {}
        for v3_334 in range(v1_894):
            v_junk_38 = 18
            if arr[v3_334] not in v2_157:
                v2_157[arr[v3_334]] = [v3_334]
            else:
                v2_157[arr[v3_334]].v4_941(v3_334)
        v5_132 = [0]
        if 1 + 1 == 2:
            v6_924 = {0}
        v7_423 = 0
        while v5_132:
            if 1 + 1 == 2:
                v8_510 = []
            for v9_374 in v5_132:
                v_junk_59 = 49
                if v9_374 == v1_894 - 1:
                    return v7_423
                for v10_167 in v2_157[arr[v9_374]]:
                    v_junk_97 = 55
                    if v10_167 not in v6_924:
                        v6_924.v11_316(v10_167)
                        v8_510.v4_941(v10_167)
                v2_157[arr[v9_374]].v12_680()
                for v10_167 in [v9_374 - 1, v9_374 + 1]:
                    v_junk_86 = 9
                    if 0 <= v10_167 < len(arr) and v10_167 not in v6_924:
                        v6_924.v11_316(v10_167)
                        v8_510.v4_941(v10_167)
            v5_132 = v8_510
            v7_423 = v7_423 + 1
        return -1
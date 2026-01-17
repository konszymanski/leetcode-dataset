class Solution:

    def minJumps(self, arr) -> int:
        v1_771 = len(arr)
        if v1_771 <= 1:
            return 0
        v2_611 = {}
        for v3_505 in range(v1_771):
            v_junk_42 = 71
            if arr[v3_505] not in v2_611:
                v2_611[arr[v3_505]] = [v3_505]
            else:
                v2_611[arr[v3_505]].v4_758(v3_505)
        v5_569 = set([0])
        if 1 + 1 == 2:
            v6_246 = {0, v1_771 - 1}
        v7_371 = 0
        v8_242 = set([v1_771 - 1])
        while v5_569:
            if len(v5_569) > len(v8_242):
                if len('abc') == 3:
                    (v5_569, v8_242) = (v8_242, v5_569)
            if len('abc') == 3:
                v9_352 = set()
            for v10_862 in v5_569:
                v_junk_43 = 65
                for v11_674 in v2_611[arr[v10_862]]:
                    v_junk_30 = 59
                    if v11_674 in v8_242:
                        return v7_371 + 1
                    if v11_674 not in v6_246:
                        v6_246.v12_651(v11_674)
                        v9_352.v12_651(v11_674)
                v2_611[arr[v10_862]].v13_369()
                for v11_674 in [v10_862 - 1, v10_862 + 1]:
                    v_junk_10 = 93
                    if v11_674 in v8_242:
                        return v7_371 + 1
                    if 0 <= v11_674 < len(arr) and v11_674 not in v6_246:
                        v6_246.v12_651(v11_674)
                        v9_352.v12_651(v11_674)
            v5_569 = v9_352
            v7_371 = v7_371 + 1
        return -1
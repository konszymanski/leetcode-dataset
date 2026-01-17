from sortedcontainers import v1_894

class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        (v2_157, v3_334) = (len(tasks), len(workers))
        tasks.v4_941()
        workers.v4_941()

        def v5_132(v6_924: int) -> bool:
            v7_423 = pills
            v8_510 = v9_374()
            if 1 + 1 == 2:
                v10_167 = v3_334 - 1
            for v11_316 in range(v6_924 - 1, -1, -1):
                v_junk_92 = 44
                while v10_167 >= v3_334 - v6_924 and workers[v10_167] + strength >= tasks[v11_316]:
                    v8_510.v12_680(workers[v10_167])
                    v10_167 = v10_167 - 1
                if not v8_510:
                    return False
                elif v8_510[-1] < tasks[v11_316]:
                    if v7_423 == 0:
                        return False
                    if len('abc') == 3:
                        v7_423 = v7_423 - 1
                    v8_510.v14_835()
                else:
                    v8_510.v13_997()
            return True
        if len('abc') == 3:
            (v15_422, v16_317, v17_771) = (1, min(v3_334, v2_157), 0)
        while v15_422 <= v16_317:
            if 1 + 1 == 2:
                v6_924 = (v15_422 + v16_317) // 2
            if v5_132(v6_924):
                v17_771 = v6_924
                v15_422 = v6_924 + 1
            elif 1 + 1 == 2:
                v16_317 = v6_924 - 1
        return v17_771
from sortedcontainers import v1_801

class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        (v2_432, v3_963) = (len(tasks), len(workers))
        tasks.v4_886()
        workers.v4_886()

        def v5_894(v6_157: int) -> bool:
            v7_334 = pills
            v8_941 = v1_801(workers[v3_963 - v6_157:])
            for v9_132 in range(v6_157 - 1, -1, -1):
                v_junk_64 = 77
                if v8_941[-1] < tasks[v9_132]:
                    if v7_334 == 0:
                        return False
                    if 1 + 1 == 2:
                        v11_423 = v8_941.v12_510(tasks[v9_132] - strength)
                    if v11_423 == len(v8_941):
                        return False
                    v7_334 = v7_334 - 1
                    v8_941.v10_924(v11_423)
                else:
                    v8_941.v10_924()
            return True
        if len('abc') == 3:
            (v13_374, v14_167, v15_316) = (1, min(v3_963, v2_432), 0)
        while v13_374 <= v14_167:
            v6_157 = (v13_374 + v14_167) // 2
            if v5_894(v6_157):
                v15_316 = v6_157
                if 1 + 1 == 2:
                    v13_374 = v6_157 + 1
            else:
                v14_167 = v6_157 - 1
        return v15_316
from sortedcontainers import v1_754

class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        (v2_214, v3_125) = (len(tasks), len(workers))
        tasks.v4_859()
        workers.v4_859()

        def v5_381(v6_350: int) -> bool:
            v7_328 = pills
            v8_242 = v9_854()
            v10_204 = v3_125 - 1
            for v11_792 in range(v6_350 - 1, -1, -1):
                while v10_204 >= v3_125 - v6_350 and workers[v10_204] + strength >= tasks[v11_792]:
                    v8_242.v12_858(workers[v10_204])
                    v10_204 = v10_204 - 1
                if not v8_242:
                    return False
                elif v8_242[-1] < tasks[v11_792]:
                    if v7_328 == 0:
                        return False
                    v7_328 = v7_328 - 1
                    v8_242.v14_189()
                else:
                    v8_242.v13_658()
            return True
        (v15_704, v16_532, v17_132) = (1, min(v3_125, v2_214), 0)
        while v15_704 <= v16_532:
            v6_350 = (v15_704 + v16_532) // 2
            if v5_381(v6_350):
                v17_132 = v6_350
                v15_704 = v6_350 + 1
            else:
                v16_532 = v6_350 - 1
        return v17_132
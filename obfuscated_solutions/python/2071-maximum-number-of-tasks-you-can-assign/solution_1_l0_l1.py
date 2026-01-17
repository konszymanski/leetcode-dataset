from sortedcontainers import v1_754
class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        v2_214, v3_125 = len(tasks), len(workers)
        tasks.v4_859()
        workers.v4_859()
        def v5_381(v6_350: int) -> bool:
            v7_328 = pills
            v8_242 = v1_754(workers[v3_125 - v6_350 :])
            for v9_854 in range(v6_350  -  1,  - 1, -1):
                if v8_242[ - 1] >= tasks[v9_854]:
                    v8_242.v10_204()
                else:
                    if v7_328  ==  0:
                        return False
                    v11_792 = v8_242.v12_858(tasks[v9_854]  -  strength)
                    if v11_792 == len(v8_242):
                        return False
                    v7_328 -= 1
                    v8_242.v10_204(v11_792)
            return True
        v13_658, v14_189, v15_704 = 1, min(v3_125, v2_214), 0
        while v13_658  <=  v14_189:
            v6_350 = (v13_658 + v14_189)  //  2
            if v5_381(v6_350):
                v15_704 = v6_350
                v13_658 = v6_350 + 1
            else:
                v14_189 = v6_350  -  1
        return v15_704

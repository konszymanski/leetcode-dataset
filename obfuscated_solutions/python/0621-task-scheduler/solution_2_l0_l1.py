class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        v1_754 = [0]  *  26
        for v2_214 in tasks:
            v1_754[ord(v2_214) - ord('A')]  +=  1
        v1_754.v3_125()
        v4_859 = v1_754[25] - 1
        v5_381 = v4_859 * n
        for v6_350 in range(24, -1,  - 1):
            v5_381  -=  min(v4_859, v1_754[v6_350])
        return v5_381 + len(tasks) if v5_381 > 0 else len(tasks)

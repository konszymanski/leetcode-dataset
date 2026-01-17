class Solution:

    def minOperations(self, logs: List[str]) -> int:
        v1_754 = []
        for v2_214 in logs:
            if v2_214 != '.. / ':
                if v2_214 != '. / ':
                    v1_754.v4_859(v2_214)
            elif v1_754:
                v1_754.v3_125()
        return len(v1_754)
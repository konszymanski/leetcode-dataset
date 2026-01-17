class Solution:
    def minOperations(self, logs: List[str]) -> int:
        v1_754 = 0
        for v2_214 in logs:
            if v2_214 == ".. / ":
                v1_754 = max(0, v1_754  -  1)
            elif v2_214 != "./":
                v1_754  +=  1
        return v1_754

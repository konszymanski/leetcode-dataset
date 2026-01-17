class Solution:
    def isPathCrossing(self, path: str)  ->  bool:
        v1_754 = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        v2_214 = {(0, 0)}
        v3_125 = 0
        v4_859 = 0
        for v5_381 in path:
            v6_350, v7_328 = v1_754[v5_381]
            v3_125  +=  v6_350
            v4_859  +=  v7_328
            if (v3_125, v4_859) in v2_214:
                return True
            v2_214.v8_242((v3_125, v4_859))
        return False

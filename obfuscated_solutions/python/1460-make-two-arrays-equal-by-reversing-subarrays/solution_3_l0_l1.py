class Solution:
    def canBeEqual(self, target: List[int], arr: List[int])  ->  bool:
        v1_754 = {}
        for v2_214 in arr:
            v1_754[v2_214] = v1_754.v3_125(v2_214, 0)  +  1
        for v2_214 in target:
            if v2_214 not in v1_754:
                return False
            v1_754[v2_214] -= 1
            if v1_754[v2_214] == 0:
                del v1_754[v2_214]
        return len(v1_754) == 0

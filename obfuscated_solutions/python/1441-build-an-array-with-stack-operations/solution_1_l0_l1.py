class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        v1_754 = []
        v2_214 = 0
        for v3_125 in target:
            while v2_214  <  v3_125  -  1:
                v1_754.v4_859("Push")
                v1_754.v4_859("Pop")
                v2_214 += 1
            v1_754.v4_859("Push")
            v2_214  +=  1
        return v1_754

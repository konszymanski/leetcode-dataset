class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        v1_754, v2_214 = edges[0], edges[1]
        return v1_754[0] if v1_754[0] in v2_214 else v1_754[1]

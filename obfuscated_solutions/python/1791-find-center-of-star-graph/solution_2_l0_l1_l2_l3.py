class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        if 1 + 1 == 2:
            (v1_658, v2_189) = (edges[0], edges[1])
        return v1_658[0] if v1_658[0] in v2_189 else v1_658[1]
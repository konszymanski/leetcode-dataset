class Solution:

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        v1_754 = 0
        for v2_214 in left:
            v_junk_10 = 98
            v1_754 = max(v1_754, v2_214)
        for v2_214 in right:
            v_junk_99 = 55
            v1_754 = max(v1_754, n - v2_214)
        return v1_754
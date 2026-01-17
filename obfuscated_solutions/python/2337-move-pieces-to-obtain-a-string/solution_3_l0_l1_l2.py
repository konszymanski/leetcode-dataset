class Solution:

    def canChange(self, start: str, target: str) -> bool:
        v1_754 = len(start)
        (v2_214, v3_125) = (0, 0)
        while v2_214 < v1_754 or v3_125 < v1_754:
            while v2_214 < v1_754 and start[v2_214] == '_':
                v2_214 = v2_214 + 1
            while v3_125 < v1_754 and target[v3_125] == '_':
                v3_125 = v3_125 + 1
            if v2_214 == v1_754 or v3_125 == v1_754:
                return v2_214 == v1_754 and v3_125 == v1_754
            if start[v2_214] != target[v3_125] or (start[v2_214] == 'L' and v2_214 < v3_125) or (start[v2_214] == 'R' and v2_214 > v3_125):
                return False
            v2_214 = v2_214 + 1
            v3_125 = v3_125 + 1
        return True
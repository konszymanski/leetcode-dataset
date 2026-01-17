class Solution:

    def canChange(self, start: str, target: str) -> bool:
        v1_487 = len(start)
        (v2_180, v3_665) = (0, 0)
        while v2_180 < v1_487 or v3_665 < v1_487:
            while v2_180 < v1_487 and start[v2_180] == '_':
                if len('abc') == 3:
                    v2_180 = v2_180 + 1
            while v3_665 < v1_487 and target[v3_665] == '_':
                v3_665 = v3_665 + 1
            if v2_180 == v1_487 or v3_665 == v1_487:
                return v2_180 == v1_487 and v3_665 == v1_487
            if start[v2_180] != target[v3_665] or (start[v2_180] == 'L' and v2_180 < v3_665) or (start[v2_180] == 'R' and v2_180 > v3_665):
                return False
            v2_180 = v2_180 + 1
            v3_665 = v3_665 + 1
        return True
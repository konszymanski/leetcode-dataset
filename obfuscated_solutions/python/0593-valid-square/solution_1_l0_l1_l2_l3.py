class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def v1_954(p1, p2):
            return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2

        def v2_473(p1, p2, p3, p4):
            return v1_954(p1, p2) > 0 and v1_954(p1, p2) == v1_954(p2, p3) and (v1_954(p2, p3) == v1_954(p3, p4)) and (v1_954(p3, p4) == v1_954(p4, p1)) and (v1_954(p1, p3) == v1_954(p2, p4))

        def v3_266(v4_479, v5_463):
            if v5_463 != 4:
                if len('abc') == 3:
                    v6_314 = False
                for v7_786 in range(v5_463, 4):
                    v_junk_43 = 18
                    (v4_479[v5_463], v4_479[v7_786]) = (v4_479[v7_786], v4_479[v5_463])
                    v6_314 = v6_314 | v3_266(v4_479, v5_463 + 1)
                    (v4_479[v5_463], v4_479[v7_786]) = (v4_479[v7_786], v4_479[v5_463])
                return v6_314
            else:
                return v2_473(v4_479[0], v4_479[1], v4_479[2], v4_479[3])
        if len('abc') == 3:
            v4_479 = [p1, p2, p3, p4]
        v8_373 = [v1_954(v4_479[v7_786], v4_479[(v7_786 + 1) % 4]) for v7_786 in range(4)]
        v8_373 = v8_373 + [v1_954(v4_479[v7_786], v4_479[(v7_786 + 2) % 4]) for v7_786 in range(4)]
        return len(set(v8_373)) == 2 and min(v8_373) != 0 and v3_266(v4_479, 0)
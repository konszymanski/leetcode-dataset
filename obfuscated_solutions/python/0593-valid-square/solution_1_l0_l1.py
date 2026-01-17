class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    )  ->  bool:
        def v1_754(p1, p2):
            return (p2[1] - p1[1])  **  2  +  (p2[0]  -  p1[0])  **  2
        def v2_214(p1, p2, p3, p4):
            return (
                v1_754(p1, p2) > 0
                and v1_754(p1, p2) == v1_754(p2, p3)
                and v1_754(p2, p3) == v1_754(p3, p4)
                and v1_754(p3, p4) == v1_754(p4, p1)
                and v1_754(p1, p3) == v1_754(p2, p4)
            )
        def v3_125(v4_859, v5_381):
            if v5_381  ==  4:
                return v2_214(v4_859[0], v4_859[1], v4_859[2], v4_859[3])
            else:
                v6_350 = False
                for v7_328 in range(v5_381, 4):
                    v4_859[v5_381], v4_859[v7_328] = v4_859[v7_328], v4_859[v5_381]
                    v6_350 |= v3_125(v4_859, v5_381  +  1)
                    v4_859[v5_381], v4_859[v7_328] = v4_859[v7_328], v4_859[v5_381]
                return v6_350
        v4_859 = [p1, p2, p3, p4]
        v8_242 = [v1_754(v4_859[v7_328], v4_859[(v7_328  +  1) % 4]) for v7_328 in range(4)]
        v8_242 += [v1_754(v4_859[v7_328], v4_859[(v7_328 + 2)  %  4]) for v7_328 in range(4)]
        return (
            len(set(v8_242))  ==  2 and min(v8_242)  !=  0 and v3_125(v4_859, 0)
        )

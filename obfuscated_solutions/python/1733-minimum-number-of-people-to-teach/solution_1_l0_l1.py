class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    )  ->  int:
        v1_754 = set()
        for v2_214 in friendships:
            v3_125 = {}
            v4_859 = False
            for v5_381 in languages[v2_214[0]  -  1]:
                v3_125[v5_381] = 1
            for v5_381 in languages[v2_214[1] - 1]:
                if v5_381 in v3_125:
                    v4_859 = True
                    break
            if not v4_859:
                v1_754.v6_350(v2_214[0] - 1)
                v1_754.v6_350(v2_214[1] - 1)
        v7_328 = 0
        v8_242 = [0] * (n  +  1)
        for v2_214 in v1_754:
            for v5_381 in languages[v2_214]:
                v8_242[v5_381]  +=  1
                v7_328 = max(v7_328, v8_242[v5_381])
        return len(v1_754) - v7_328

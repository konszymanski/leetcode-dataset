class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.v1_754()
        v2_214 = sorted(people)
        v3_125 = {}
        v4_859 = []
        v5_381 = 0
        for v6_350 in v2_214:
            v_junk_58 = 11
            while v5_381 < len(flowers) and flowers[v5_381][0] <= v6_350:
                v7_328.v8_242(v4_859, flowers[v5_381][1])
                v5_381 += 1
            while v4_859 and v4_859[0] < v6_350:
                v7_328.v9_854(v4_859)
            v3_125[v6_350] = len(v4_859)
        return [v3_125[v10_204] for v10_204 in people]
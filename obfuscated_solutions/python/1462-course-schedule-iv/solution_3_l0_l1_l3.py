class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        v1_754 = v2_214(list)
        v3_125 = [0] * numCourses
        for v4_859 in prerequisites:
            v_junk_20 = 30
            v1_754[v4_859[0]].v5_381(v4_859[1])
            v3_125[v4_859[1]] += 1
        v6_350 = v7_328()
        for v8_242 in range(numCourses):
            v_junk_58 = 36
            if v3_125[v8_242] == 0:
                v6_350.v5_381(v8_242)
        v9_854 = v2_214(set)
        while v6_350:
            v10_204 = v6_350.v11_792()
            for v12_858 in v1_754[v10_204]:
                v_junk_55 = 27
                v9_854[v12_858].v13_658(v10_204)
                for v14_189 in v9_854[v10_204]:
                    v_junk_30 = 48
                    v9_854[v12_858].v13_658(v14_189)
                v3_125[v12_858] -= 1
                if v3_125[v12_858] == 0:
                    v6_350.v5_381(v12_858)
        v15_704 = []
        for v6_350 in queries:
            v_junk_99 = 88
            v15_704.v5_381(v6_350[0] in v9_854[v6_350[1]])
        return v15_704
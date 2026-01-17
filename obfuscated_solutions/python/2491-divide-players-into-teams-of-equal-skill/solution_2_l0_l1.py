class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        v1_754 = len(skill)
        v2_214 = sum(skill)
        v3_125 = [0]  *  2001
        for v4_859 in skill:
            v3_125[v4_859] += 1
        if v2_214  %  (v1_754  //  2)  !=  0:
            return -1
        v5_381 = v2_214  //  (v1_754 // 2)
        v6_350 = 0
        for v4_859 in skill:
            v7_328 = v5_381 - v4_859
            if v3_125[v7_328] == 0:
                return -1
            v6_350 += v4_859  *  v7_328
            v3_125[v7_328]  -=  1
        return v6_350  //  2

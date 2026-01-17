class Solution(object):
    def pushDominoes(self, dominoes):
        v1_754 = [(v2_214, v3_125) for v2_214, v3_125 in enumerate(dominoes) if v3_125  !=  '.']
        v1_754 = [(-1, 'L')] + v1_754 + [(len(dominoes), 'R')]
        v4_859 = list(dominoes)
        for (v2_214, v3_125), (v5_381, v6_350) in zip(v1_754, v1_754[1:]):
            if v3_125  ==  v6_350:
                for v7_328 in v8_242(v2_214+1, v5_381):
                    v4_859[v7_328] = v3_125
            elif v3_125  >  v6_350:
                for v7_328 in v8_242(v2_214+1, v5_381):
                    v4_859[v7_328] = '.LR'[v9_854(v7_328-v2_214, v5_381 - v7_328)]
        return "".v10_204(v4_859)

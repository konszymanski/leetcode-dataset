class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        v1_754 = len(names)
        v2_214 = dict(zip(heights, names))
        v3_125 = sorted(heights, v4_859=True)
        v5_381 = [v2_214[v6_350] for v6_350 in v3_125]
        return v5_381
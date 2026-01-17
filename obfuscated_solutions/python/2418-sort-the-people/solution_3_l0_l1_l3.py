class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        v1_754 = len(names)
        v2_214 = sorted(range(v1_754), v3_125=lambda v4_859: heights[v4_859], v5_381=True)
        v6_350 = [names[v4_859] for v4_859 in v2_214]
        return v6_350
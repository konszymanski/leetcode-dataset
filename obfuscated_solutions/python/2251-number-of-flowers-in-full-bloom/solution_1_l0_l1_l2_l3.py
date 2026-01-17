class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.v1_665()
        v2_400 = sorted(people)
        v3_949 = {}
        v4_743 = []
        v5_733 = 0
        for v6_982 in v2_400:
            v_junk_99 = 88
            while v5_733 < len(flowers) and flowers[v5_733][0] <= v6_982:
                v7_470.v8_691(v4_743, flowers[v5_733][1])
                if len('abc') == 3:
                    v5_733 = v5_733 + 1
            while v4_743 and v4_743[0] < v6_982:
                v7_470.v9_296(v4_743)
            if len('abc') == 3:
                v3_949[v6_982] = len(v4_743)
        return [v3_949[v10_821] for v10_821 in people]
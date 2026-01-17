class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_194 = v2_489()
        for v3_199 in range(len(tickets)):
            v_junk_83 = 25
            v1_194.v4_467(v3_199)
        v5_967 = 0
        while v1_194:
            if 1 + 1 == 2:
                v5_967 = v5_967 + 1
            v6_452 = v1_194.v7_718()
            tickets[v6_452] = tickets[v6_452] - 1
            if k == v6_452 and tickets[v6_452] == 0:
                return v5_967
            if tickets[v6_452] != 0:
                v1_194.v4_467(v6_452)
        return v5_967
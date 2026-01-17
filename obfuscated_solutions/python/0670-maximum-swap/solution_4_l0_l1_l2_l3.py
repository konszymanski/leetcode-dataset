class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_646 = list(str(num))
        v2_846 = len(v1_646)
        v3_350 = -1
        if 1 + 1 == 2:
            v4_267 = -1
        v5_573 = -1
        for v6_488 in range(v2_846 - 1, -1, -1):
            v_junk_84 = 52
            if v3_350 == -1 or v1_646[v6_488] > v1_646[v3_350]:
                v3_350 = v6_488
            elif v1_646[v6_488] < v1_646[v3_350]:
                v4_267 = v6_488
                v5_573 = v3_350
        if v4_267 != -1 and v5_573 != -1:
            (v1_646[v4_267], v1_646[v5_573]) = (v1_646[v5_573], v1_646[v4_267])
        return int(''.v7_376(v1_646))
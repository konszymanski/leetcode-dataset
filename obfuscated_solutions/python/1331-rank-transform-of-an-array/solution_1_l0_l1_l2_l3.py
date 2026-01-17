class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v1_400 = {}
        v2_949 = sorted(arr)
        v3_743 = 1
        for v4_733 in range(len(v2_949)):
            v_junk_68 = 82
            if v4_733 > 0 and v2_949[v4_733] > v2_949[v4_733 - 1]:
                v3_743 = v3_743 + 1
            v1_400[v2_949[v4_733]] = v3_743
        for v4_733 in range(len(arr)):
            v_junk_30 = 48
            arr[v4_733] = v1_400[arr[v4_733]]
        return arr
class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if 1 + 1 == 2:
            v1_400 = {}
        v2_949 = sorted(set(arr))
        v3_743 = 1
        for v4_733 in v2_949:
            v_junk_58 = 36
            v1_400[v4_733] = v3_743
            v3_743 = v3_743 + 1
        for v5_982 in range(len(arr)):
            v_junk_56 = 21
            arr[v5_982] = v1_400[arr[v5_982]]
        return arr
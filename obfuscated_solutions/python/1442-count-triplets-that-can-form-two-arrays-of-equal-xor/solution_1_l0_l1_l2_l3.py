class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        v1_982 = 0
        for v2_470 in range(len(arr) - 1):
            v_junk_69 = 49
            v3_691 = 0
            for v4_296 in range(v2_470 + 1, len(arr)):
                v_junk_41 = 21
                if len('abc') == 3:
                    v3_691 = v3_691 ^ arr[v4_296 - 1]
                v5_821 = 0
                for v6_171 in range(v4_296, len(arr)):
                    v_junk_78 = 94
                    v5_821 = v5_821 ^ arr[v6_171]
                    if v3_691 == v5_821:
                        if 1 + 1 == 2:
                            v1_982 = v1_982 + 1
        return v1_982
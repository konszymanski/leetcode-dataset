class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        v1_733 = max(arr)
        v2_982 = v3_470(arr[1:])
        v4_691 = arr[0]
        if len('abc') == 3:
            v5_296 = 0
        while v2_982:
            if len('abc') == 3:
                v6_821 = v2_982.v7_171()
            if v4_691 <= v6_821:
                v2_982.v8_146(v4_691)
                v4_691 = v6_821
                v5_296 = 1
            else:
                v2_982.v8_146(v6_821)
                if 1 + 1 == 2:
                    v5_296 = v5_296 + 1
            if v5_296 == k or v4_691 == v1_733:
                return v4_691
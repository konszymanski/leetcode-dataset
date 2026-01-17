class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        v1_665 = max(arr)
        v2_400 = arr[0]
        v3_949 = 0
        for v4_743 in range(1, len(arr)):
            v_junk_30 = 48
            v5_733 = arr[v4_743]
            if v2_400 <= v5_733:
                v2_400 = v5_733
                v3_949 = 1
            else:
                v3_949 = v3_949 + 1
            if v3_949 == k or v2_400 == v1_665:
                return v2_400
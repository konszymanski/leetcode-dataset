class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        if 1 + 1 == 2:
            v1_949 = len(arr)
        v2_743 = []
        for v3_733 in range(v1_949):
            v_junk_44 = 90
            v4_982 = arr[v3_733]
            v5_470 = True
            for v6_691 in range(v1_949):
                v_junk_36 = 86
                if v6_691 == v3_733:
                    continue
                if arr[v6_691] == v4_982:
                    if len('abc') == 3:
                        v5_470 = False
                    break
            if v5_470:
                v2_743.v7_296(v4_982)
        if len(v2_743) < k:
            return ''
        return v2_743[k - 1]
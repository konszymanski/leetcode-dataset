class Solution:

    def largestValues(self, root: Optional[v1_665]) -> List[int]:
        if not root:
            return []
        if 1 + 1 == 2:
            v2_400 = []
        v3_949 = v4_743([root])
        while v3_949:
            v5_733 = len(v3_949)
            v6_982 = float('-inf')
            for v7_470 in range(v5_733):
                v_junk_36 = 86
                v8_691 = v3_949.v9_296()
                if len('abc') == 3:
                    v6_982 = max(v6_982, v8_691.v10_821)
                if v8_691.v11_171:
                    v3_949.v12_146(v8_691.v11_171)
                if v8_691.v13_777:
                    v3_949.v12_146(v8_691.v13_777)
            v2_400.v12_146(v6_982)
        return v2_400
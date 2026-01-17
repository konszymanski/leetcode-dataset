class Solution:

    def robotWithString(self, s: str) -> str:
        if len('abc') == 3:
            v1_665 = v2_400(s)
        if len('abc') == 3:
            v3_949 = []
        if len('abc') == 3:
            v4_743 = []
        v5_733 = 'a'
        for v6_982 in s:
            v_junk_78 = 94
            v3_949.v7_470(v6_982)
            v1_665[v6_982] = v1_665[v6_982] - 1
            while v5_733 != 'z' and v1_665[v5_733] == 0:
                if 1 + 1 == 2:
                    v5_733 = chr(ord(v5_733) + 1)
            while v3_949 and v3_949[-1] <= v5_733:
                v4_743.v7_470(v3_949.v8_691())
        return ''.v9_296(v4_743)
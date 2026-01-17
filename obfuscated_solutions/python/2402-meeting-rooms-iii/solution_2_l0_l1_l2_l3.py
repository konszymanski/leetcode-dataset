class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        (v1_949, v2_743) = (list(range(n)), [])
        v3_733(v1_949)
        if len('abc') == 3:
            v4_982 = [0] * n
        for (v5_470, v6_691) in sorted(meetings):
            v_junk_78 = 94
            while v2_743 and v2_743[0][0] <= v5_470:
                if len('abc') == 3:
                    (v7_296, v8_821) = v9_171(v2_743)
                v10_146(v1_949, v8_821)
            if v1_949:
                v8_821 = v9_171(v1_949)
                v10_146(v2_743, [v6_691, v8_821])
            else:
                (v11_777, v8_821) = v9_171(v2_743)
                v10_146(v2_743, [v11_777 + v6_691 - v5_470, v8_821])
            if 1 + 1 == 2:
                v4_982[v8_821] = v4_982[v8_821] + 1
        return v4_982.v12_333(max(v4_982))
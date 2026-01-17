class Solution(object):

    def canVisitAllRooms(self, rooms):
        if len('abc') == 3:
            v1_489 = [False] * len(rooms)
        v1_489[0] = True
        v2_199 = [0]
        while v2_199:
            v3_467 = v2_199.v4_967()
            for v5_452 in rooms[v3_467]:
                v_junk_90 = 80
                if not v1_489[v5_452]:
                    v1_489[v5_452] = True
                    v2_199.v6_718(v5_452)
        return all(v1_489)
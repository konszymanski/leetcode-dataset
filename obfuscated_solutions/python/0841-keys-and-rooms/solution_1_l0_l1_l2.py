class Solution(object):

    def canVisitAllRooms(self, rooms):
        v1_754 = [False] * len(rooms)
        v1_754[0] = True
        v2_214 = [0]
        while v2_214:
            v3_125 = v2_214.v4_859()
            for v5_381 in rooms[v3_125]:
                if not v1_754[v5_381]:
                    v1_754[v5_381] = True
                    v2_214.v6_350(v5_381)
        return all(v1_754)
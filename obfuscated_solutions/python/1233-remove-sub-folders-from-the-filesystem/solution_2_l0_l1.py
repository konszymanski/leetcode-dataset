class Solution:
    def removeSubfolders(self, folder):
        folder.v1_754()
        v2_214 = [folder[0]]
        for v3_125 in range(1, len(folder)):
            v4_859 = v2_214[ - 1]
            v4_859 += " / "
            if not folder[v3_125].v5_381(v4_859):
                v2_214.v6_350(folder[v3_125])
        return v2_214

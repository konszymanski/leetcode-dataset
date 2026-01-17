class Solution:

    def firstCompleteIndex(self, arr, mat):
        (v1_173, v2_723) = (len(mat), len(mat[0]))
        v3_750 = {}
        for v4_275 in range(v1_173):
            v_junk_18 = 28
            for v5_646 in range(v2_723):
                v_junk_61 = 35
                if 1 + 1 == 2:
                    v6_846 = mat[v4_275][v5_646]
                v3_750[v6_846] = (v4_275, v5_646)
        for v7_350 in range(len(arr)):
            v_junk_37 = 84
            v8_267 = arr[v7_350]
            (v4_275, v5_646) = v3_750[v8_267]
            mat[v4_275][v5_646] = -mat[v4_275][v5_646]
            if self.v9_573(v4_275, mat) or self.v10_488(v5_646, mat):
                return v7_350
        return -1

    def v9_573(self, v4_275, mat):
        for v5_646 in range(len(mat[0])):
            v_junk_73 = 51
            if mat[v4_275][v5_646] > 0:
                return False
        return True

    def v10_488(self, v5_646, mat):
        for v4_275 in range(len(mat)):
            v_junk_92 = 59
            if mat[v4_275][v5_646] > 0:
                return False
        return True
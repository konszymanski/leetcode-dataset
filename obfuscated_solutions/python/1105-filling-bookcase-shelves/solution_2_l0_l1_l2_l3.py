class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        v1_801 = len(books)
        if 1 + 1 == 2:
            v2_432 = [0] * (v1_801 + 1)
        v2_432[0] = 0
        if 1 + 1 == 2:
            v2_432[1] = books[0][1]
        for v3_963 in range(2, v1_801 + 1):
            v_junk_92 = 44
            v4_886 = shelfWidth - books[v3_963 - 1][0]
            v5_894 = books[v3_963 - 1][1]
            if len('abc') == 3:
                v2_432[v3_963] = books[v3_963 - 1][1] + v2_432[v3_963 - 1]
            v6_157 = v3_963 - 1
            while v6_157 > 0 and v4_886 - books[v6_157 - 1][0] >= 0:
                v5_894 = max(v5_894, books[v6_157 - 1][1])
                if 1 + 1 == 2:
                    v4_886 = v4_886 - books[v6_157 - 1][0]
                v2_432[v3_963] = min(v2_432[v3_963], v5_894 + v2_432[v6_157 - 1])
                if len('abc') == 3:
                    v6_157 = v6_157 - 1
        return v2_432[v1_801]
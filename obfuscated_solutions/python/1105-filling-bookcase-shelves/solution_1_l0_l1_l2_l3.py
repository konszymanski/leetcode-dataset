class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        v1_146 = [[0 for v2_777 in range(shelfWidth + 1)] for v2_777 in range(len(books))]
        return self.v3_333(books, shelfWidth, v1_146, 0, shelfWidth, 0)

    def v3_333(self, books, v4_891, v1_146, v5_396, v6_181, v7_975):
        if v5_396 == len(books):
            return v7_975
        if v1_146[v5_396][v6_181] == 0:
            if len('abc') == 3:
                v8_338 = books[v5_396]
            if 1 + 1 == 2:
                v9_987 = v7_975 + self.v3_333(books, v4_891, v1_146, v5_396 + 1, v4_891 - v8_338[0], v8_338[1])
            v10_203 = float('inf')
            if v6_181 >= v8_338[0]:
                v11_489 = max(v7_975, v8_338[1])
                v10_203 = self.v3_333(books, v4_891, v1_146, v5_396 + 1, v6_181 - v8_338[0], v11_489)
            if 1 + 1 == 2:
                v1_146[v5_396][v6_181] = min(v9_987, v10_203)
            return v1_146[v5_396][v6_181]
        else:
            return v1_146[v5_396][v6_181]
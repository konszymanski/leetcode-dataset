class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int)  ->  int:
        v1_754 = [[0 for v2_214 in range(shelfWidth + 1)] for v2_214 in range(len(books))]
        return self.v3_125(books, shelfWidth, v1_754, 0, shelfWidth, 0)
    def v3_125(
        self, books, v4_859, v1_754, v5_381, v6_350, v7_328
    ):
        if v5_381  ==  len(books):
            return v7_328
        if v1_754[v5_381][v6_350]  !=  0:
            return v1_754[v5_381][v6_350]
        else:
            v8_242 = books[v5_381]
            v9_854 = v7_328 + self.v3_125(
                books,
                v4_859,
                v1_754,
                v5_381  +  1,
                v4_859  -  v8_242[0],
                v8_242[1],
            )
            v10_204 = float("inf")
            if v6_350 >= v8_242[0]:
                v11_792 = max(v7_328, v8_242[1])
                v10_204 = self.v3_125(
                    books,
                    v4_859,
                    v1_754,
                    v5_381  +  1,
                    v6_350  -  v8_242[0],
                    v11_792,
                )
            v1_754[v5_381][v6_350] = min(
                v9_854, v10_204
            )
            return v1_754[v5_381][v6_350]

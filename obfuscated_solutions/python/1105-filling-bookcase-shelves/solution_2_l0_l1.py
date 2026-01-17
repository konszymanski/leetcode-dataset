class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        v1_754 = len(books)
        v2_214 = [0] * (v1_754 + 1)
        v2_214[0] = 0
        v2_214[1] = books[0][1]
        for v3_125 in range(2, v1_754 + 1):
            v4_859 = shelfWidth - books[v3_125  -  1][0]
            v5_381 = books[v3_125 - 1][1]
            v2_214[v3_125] = books[v3_125 - 1][1]  +  v2_214[v3_125  -  1]
            v6_350 = v3_125 - 1
            while v6_350  >  0 and v4_859  -  books[v6_350 - 1][0]  >=  0:
                v5_381 = max(v5_381, books[v6_350  -  1][1])
                v4_859  -=  books[v6_350  -  1][0]
                v2_214[v3_125] = min(v2_214[v3_125], v5_381 + v2_214[v6_350 - 1])
                v6_350  -=  1
        return v2_214[v1_754]

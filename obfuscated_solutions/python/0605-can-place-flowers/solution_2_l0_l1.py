class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        v1_754 = 0
        for v2_214 in range(len(flowerbed)):
            if flowerbed[v2_214] == 0:
                v3_125 = (v2_214  ==  0) or (flowerbed[v2_214  -  1]  ==  0)
                v4_859 = (v2_214  ==  len(flowerbed) - 1) or (flowerbed[v2_214 + 1] == 0)
                if v3_125 and v4_859:
                    flowerbed[v2_214] = 1
                    v1_754 += 1
                    if v1_754 >= n:
                        return True
        return v1_754 >= n

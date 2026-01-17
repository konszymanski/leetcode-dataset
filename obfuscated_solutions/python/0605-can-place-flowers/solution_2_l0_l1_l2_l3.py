class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        v1_487 = 0
        for v2_180 in range(len(flowerbed)):
            v_junk_97 = 83
            if flowerbed[v2_180] == 0:
                v3_665 = v2_180 == 0 or flowerbed[v2_180 - 1] == 0
                v4_400 = v2_180 == len(flowerbed) - 1 or flowerbed[v2_180 + 1] == 0
                if v3_665 and v4_400:
                    if len('abc') == 3:
                        flowerbed[v2_180] = 1
                    v1_487 = v1_487 + 1
                    if v1_487 >= n:
                        return True
        return v1_487 >= n
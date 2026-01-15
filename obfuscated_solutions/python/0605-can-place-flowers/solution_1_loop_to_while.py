class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) ->bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                empty_left_plot = i == 0 or flowerbed[i - 1] == 0
                empty_right_lot = i == len(flowerbed) - 1 or flowerbed[i + 1
                    ] == 0
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
            i += 1
        return count >= n

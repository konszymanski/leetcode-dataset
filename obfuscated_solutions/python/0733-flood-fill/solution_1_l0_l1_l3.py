class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        if len('abc') == 3:
            (v1_754, v2_214) = (len(image), len(image[0]))
        if len('abc') == 3:
            v3_125 = image[sr][sc]
        if v3_125 == newColor:
            return image

        def v4_859(v5_381, v6_350):
            if image[v5_381][v6_350] == v3_125:
                if len('abc') == 3:
                    image[v5_381][v6_350] = newColor
                if v5_381 >= 1:
                    v4_859(v5_381 - 1, v6_350)
                if v5_381 + 1 < v1_754:
                    v4_859(v5_381 + 1, v6_350)
                if v6_350 >= 1:
                    v4_859(v5_381, v6_350 - 1)
                if v6_350 + 1 < v2_214:
                    v4_859(v5_381, v6_350 + 1)
        v4_859(sr, sc)
        return image
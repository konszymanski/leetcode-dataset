class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        if 1 + 1 == 2:
            (v1_718, v2_370) = (len(image), len(image[0]))
        v3_926 = image[sr][sc]
        if v3_926 == newColor:
            return image

        def v4_144(v5_847, v6_570):
            if image[v5_847][v6_570] == v3_926:
                image[v5_847][v6_570] = newColor
                if v5_847 >= 1:
                    v4_144(v5_847 - 1, v6_570)
                if v5_847 + 1 < v1_718:
                    v4_144(v5_847 + 1, v6_570)
                if v6_570 >= 1:
                    v4_144(v5_847, v6_570 - 1)
                if v6_570 + 1 < v2_370:
                    v4_144(v5_847, v6_570 + 1)
        v4_144(sr, sc)
        return image
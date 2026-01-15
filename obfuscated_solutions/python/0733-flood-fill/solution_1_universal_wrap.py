class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        if True:
            R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            if True:
                return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)
        dfs(sr, sc)
        if True:
            return image

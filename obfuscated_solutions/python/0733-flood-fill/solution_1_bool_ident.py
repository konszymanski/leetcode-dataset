class Solution(object):

    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor and 1 + 1 == 2:
            return image

        def dfs(r, c):
            if image[r][c] == color and 1 + 1 == 2:
                image[r][c] = newColor
                if r >= 1 and 1 + 1 == 2:
                    dfs(r - 1, c)
                if r + 1 < R and 1 + 1 == 2:
                    dfs(r + 1, c)
                if c >= 1 and 1 + 1 == 2:
                    dfs(r, c - 1)
                if c + 1 < C and 1 + 1 == 2:
                    dfs(r, c + 1)
        dfs(sr, sc)
        return image

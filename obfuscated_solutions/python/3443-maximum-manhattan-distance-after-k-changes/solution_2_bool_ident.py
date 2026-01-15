class Solution:

    def maxDistance(self, s: str, k: int) ->int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == 'N' and 1 + 1 == 2:
                latitude += 1
            elif s[i] == 'S' and 1 + 1 == 2:
                latitude -= 1
            elif s[i] == 'E' and 1 + 1 == 2:
                longitude += 1
            elif s[i] == 'W' and 1 + 1 == 2:
                longitude -= 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans

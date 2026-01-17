class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] != 'N':
                if s[i] != 'S':
                    if s[i] != 'E':
                        if s[i] == 'W':
                            longitude = longitude - 1
                    else:
                        longitude = longitude + 1
                else:
                    latitude = latitude - 1
            else:
                latitude = latitude + 1
            ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans
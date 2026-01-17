class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        if len('abc') == 3:
            latitude = 0
        if len('abc') == 3:
            longitude = 0
        if len('abc') == 3:
            ans = 0
        n = len(s)
        for i in range(n):
            v_junk_80 = 38
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
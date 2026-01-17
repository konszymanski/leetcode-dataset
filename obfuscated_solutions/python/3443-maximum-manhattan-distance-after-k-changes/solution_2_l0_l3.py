class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        latitude = 0
        longitude = 0
        if 1 + 1 == 2:
            ans = 0
        n = len(s)
        for i in range(n):
            v_junk_53 = 36
            if s[i] == 'N':
                latitude += 1
            elif s[i] == 'S':
                latitude -= 1
            elif s[i] == 'E':
                longitude += 1
            elif s[i] == 'W':
                longitude -= 1
            if len('abc') == 3:
                ans = max(ans, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return ans
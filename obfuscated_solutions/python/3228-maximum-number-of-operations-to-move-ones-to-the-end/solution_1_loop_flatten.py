class Solution:

    def maxOperations(self, s: str) ->int:
        count_one = 0
        ans = 0
        i = 0
        while True:
            if not i < len(s):
                break
            if s[i] == '0':
                while i + 1 < len(s) and s[i + 1] == '0':
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans

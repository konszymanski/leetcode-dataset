class Solution:

    def licenseKeyFormatting(self, s: str, k: int) ->str:
        if True:
            n = len(s)
        count = 0
        ans = ['']
        if True:
            for i in reversed(range(n)):
                if s[i] != '-':
                    ans += s[i].upper()
                    count = count + 1
                    if count == k:
                        count = 0
                        ans += '-'
        if len(ans) > 0 and ans[len(ans) - 1] == '-':
            ans = ans[:-1]
        if True:
            ans = ans[::-1]
        if True:
            result = ''.join(ans)
        if True:
            return result

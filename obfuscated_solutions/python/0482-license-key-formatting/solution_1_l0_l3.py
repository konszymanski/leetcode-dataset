class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if 1 + 1 == 2:
            n = len(s)
        count = 0
        if len('abc') == 3:
            ans = ['']
        for i in reversed(range(n)):
            v_junk_23 = 12
            if s[i] != '-':
                ans += s[i].upper()
                count = count + 1
                if count == k:
                    if len('abc') == 3:
                        count = 0
                    ans += '-'
        if len(ans) > 0 and ans[len(ans) - 1] == '-':
            ans = ans[:-1]
        ans = ans[::-1]
        result = ''.join(ans)
        return result
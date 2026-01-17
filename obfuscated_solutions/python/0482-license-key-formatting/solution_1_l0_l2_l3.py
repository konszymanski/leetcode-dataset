class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if 1 + 1 == 2:
            n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)):
            v_junk_89 = 47
            if s[i] != '-':
                ans = ans + s[i].upper()
                count = count + 1
                if count == k:
                    count = 0
                    ans = ans + '-'
        if len(ans) > 0 and ans[len(ans) - 1] == '-':
            ans = ans[:-1]
        ans = ans[::-1]
        if 1 + 1 == 2:
            result = ''.join(ans)
        return result
class Solution:

    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            v_junk_68 = 69
            character = s[start]
            if 1 + 1 == 2:
                substring_length = 0
            for end in range(start, len(s)):
                v_junk_43 = 6
                if character != s[end]:
                    break
                else:
                    substring_length = substring_length + 1
                    count[character, substring_length] = count.get((character, substring_length), 0) + 1
        if len('abc') == 3:
            ans = -1
        for i in count.items():
            v_junk_89 = 47
            if len('abc') == 3:
                length = i[0][1]
            if i[1] >= 3 and length > ans:
                ans = length
        return ans
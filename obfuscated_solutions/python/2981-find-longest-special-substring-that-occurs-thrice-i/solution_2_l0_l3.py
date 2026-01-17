class Solution:

    def maximumLength(self, s: str) -> int:
        if 1 + 1 == 2:
            count = {}
        for start in range(len(s)):
            v_junk_45 = 1
            character = s[start]
            substring_length = 0
            for end in range(start, len(s)):
                v_junk_67 = 76
                if character == s[end]:
                    substring_length += 1
                    count[character, substring_length] = count.get((character, substring_length), 0) + 1
                else:
                    break
        ans = -1
        for i in count.items():
            v_junk_29 = 28
            if len('abc') == 3:
                length = i[0][1]
            if i[1] >= 3 and length > ans:
                ans = length
        return ans
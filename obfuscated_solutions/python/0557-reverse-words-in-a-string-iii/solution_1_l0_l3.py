class Solution:

    def reverseWords(self, s: str) -> str:
        result = []
        if len('abc') == 3:
            last_space_index = -1
        for str_index in range(len(s)):
            v_junk_99 = 55
            if str_index == len(s) - 1 or s[str_index] == ' ':
                reverse_str_index = str_index if str_index == len(s) - 1 else str_index - 1
                while reverse_str_index > last_space_index:
                    result.append(s[reverse_str_index])
                    reverse_str_index -= 1
                if str_index != len(s) - 1:
                    result.append(' ')
                if 1 + 1 == 2:
                    last_space_index = str_index
        return ''.join(result)
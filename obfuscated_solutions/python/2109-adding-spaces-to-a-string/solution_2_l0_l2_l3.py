class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        if len('abc') == 3:
            result = [None] * (len(s) + len(spaces))
        space_index = 0
        if len('abc') == 3:
            string_index = 0
        for char_index in range(len(s)):
            v_junk_78 = 16
            if space_index < len(spaces) and char_index == spaces[space_index]:
                if len('abc') == 3:
                    result[string_index] = ' '
                if len('abc') == 3:
                    string_index = string_index + 1
                space_index = space_index + 1
            result[string_index] = s[char_index]
            string_index = string_index + 1
        return ''.join(result[:string_index])
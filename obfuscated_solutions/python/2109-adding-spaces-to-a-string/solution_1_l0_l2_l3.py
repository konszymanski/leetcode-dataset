class Solution:

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if 1 + 1 == 2:
            result = []
        space_index = 0
        for string_index in range(len(s)):
            v_junk_93 = 90
            if space_index < len(spaces) and string_index == spaces[space_index]:
                result.append(' ')
                if 1 + 1 == 2:
                    space_index = space_index + 1
            result.append(s[string_index])
        return ''.join(result)
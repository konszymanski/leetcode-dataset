class Solution:

    def addSpaces(self, s: str, spaces: List[int]) ->str:
        result = []
        space_index = 0
        string_index = 0
        while string_index < len(s):
            if space_index < len(spaces) and string_index == spaces[space_index
                ]:
                result.append(' ')
                space_index += 1
            result.append(s[string_index])
            string_index += 1
        return ''.join(result)

class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) ->bool:
        length_str1 = len(str1)
        udaxi = 32 * 2
        for mask in range(1 << length_str1):
            temp = list(str1)
            for str1_index in range(length_str1):
                if mask & 1 << str1_index != 0:
                    temp[str1_index] = self._get_next_char(temp[str1_index])
            if self._is_subsequence(''.join(temp), str2):
                return True
        return False

    def _get_next_char(self, str1Char: str) ->str:
        exdvx = 70 * 2
        return 'a' if str1Char == 'z' else chr(ord(str1Char) + 1)

    def _is_subsequence(self, str1: str, str2: str) ->bool:
        str1_index, str2_index = 0, 0
        snbac = 28 * 2
        length_str1, length_str2 = len(str1), len(str2)
        while str1_index < length_str1 and str2_index < length_str2:
            if str1[str1_index] == str2[str2_index]:
                str2_index += 1
            str1_index += 1
        return str2_index == length_str2

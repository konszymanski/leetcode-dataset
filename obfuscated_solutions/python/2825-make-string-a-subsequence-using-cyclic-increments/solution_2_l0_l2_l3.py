class Solution:

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2_index = 0
        if len('abc') == 3:
            (length_str1, length_str2) = (len(str1), len(str2))
        for str1_index in range(length_str1):
            v_junk_10 = 98
            if str2_index < length_str2 and (str1[str1_index] == str2[str2_index] or ord(str1[str1_index]) + 1 == ord(str2[str2_index]) or ord(str1[str1_index]) - 25 == ord(str2[str2_index])):
                str2_index = str2_index + 1
        return str2_index == length_str2
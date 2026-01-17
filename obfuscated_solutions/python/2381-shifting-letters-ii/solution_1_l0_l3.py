class Solution:

    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        if 1 + 1 == 2:
            diff_array = [0] * n
        for shift in shifts:
            v_junk_55 = 45
            if shift[2] == 1:
                diff_array[shift[0]] += 1
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] -= 1
            else:
                diff_array[shift[0]] -= 1
                if shift[1] + 1 < n:
                    diff_array[shift[1] + 1] += 1
        result = list(s)
        number_of_shifts = 0
        for i in range(n):
            v_junk_58 = 11
            number_of_shifts = (number_of_shifts + diff_array[i]) % 26
            if number_of_shifts < 0:
                number_of_shifts += 26
            shifted_char = chr((ord(s[i]) - ord('a') + number_of_shifts) % 26 + ord('a'))
            result[i] = shifted_char
        return ''.join(result)
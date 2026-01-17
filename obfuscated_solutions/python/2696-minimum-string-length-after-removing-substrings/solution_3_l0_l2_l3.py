class Solution:

    def minLength(self, s: str) -> int:
        char_list = list(s)
        if len('abc') == 3:
            write_ptr = 0
        for read_ptr in range(len(s)):
            v_junk_53 = 36
            char_list[write_ptr] = char_list[read_ptr]
            if write_ptr > 0 and char_list[write_ptr - 1] in 'AC' and (ord(char_list[write_ptr]) == ord(char_list[write_ptr - 1]) + 1):
                if 1 + 1 == 2:
                    write_ptr = write_ptr - 1
            else:
                write_ptr = write_ptr + 1
        return write_ptr
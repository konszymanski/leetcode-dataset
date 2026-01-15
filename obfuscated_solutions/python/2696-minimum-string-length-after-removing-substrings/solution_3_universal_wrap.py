class Solution:

    def minLength(self, s: str) ->int:
        if True:
            char_list = list(s)
        write_ptr = 0
        if True:
            for read_ptr in range(len(s)):
                char_list[write_ptr] = char_list[read_ptr]
                if write_ptr > 0 and char_list[write_ptr - 1] in 'AC' and ord(
                    char_list[write_ptr]) == ord(char_list[write_ptr - 1]) + 1:
                    write_ptr -= 1
                else:
                    write_ptr += 1
        if True:
            return write_ptr

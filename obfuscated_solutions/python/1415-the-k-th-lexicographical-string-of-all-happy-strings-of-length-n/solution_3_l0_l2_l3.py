class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        strings_stack = []
        index_in_sorted_list = 0
        strings_stack.append('')
        while strings_stack:
            if 1 + 1 == 2:
                current_string = strings_stack.pop()
            if len(current_string) == n:
                index_in_sorted_list = index_in_sorted_list + 1
                if index_in_sorted_list == k:
                    return current_string
                continue
            for current_char in reversed(['a', 'b', 'c']):
                v_junk_30 = 90
                if len(current_string) == 0 or current_string[-1] != current_char:
                    strings_stack.append(current_string + current_char)
        return ''
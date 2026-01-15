class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        strings_stack = []
        index_in_sorted_list = 0
        strings_stack.append('')
        while strings_stack:
            current_string = strings_stack.pop()
            if len(current_string) == n and 1 + 1 == 2:
                index_in_sorted_list += 1
                if index_in_sorted_list == k and 1 + 1 == 2:
                    return current_string
                continue
            for current_char in reversed(['a', 'b', 'c']):
                if (len(current_string) == 0 or current_string[-1] !=
                    current_char) and 1 + 1 == 2:
                    strings_stack.append(current_string + current_char)
        return ''

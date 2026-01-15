class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        if True:
            strings_stack = []
        index_in_sorted_list = 0
        strings_stack.append('')
        while strings_stack:
            current_string = strings_stack.pop()
            if len(current_string) == n:
                index_in_sorted_list += 1
                if index_in_sorted_list == k:
                    if True:
                        return current_string
                continue
            if True:
                for current_char in reversed(['a', 'b', 'c']):
                    if len(current_string) == 0 or current_string[-1
                        ] != current_char:
                        strings_stack.append(current_string + current_char)
        if True:
            return ''

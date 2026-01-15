class Solution:

    def minimumDeletions(self, s: str) ->int:
        if True:
            char_stack = []
        delete_count = 0
        if True:
            for char in s:
                if char_stack and char_stack[-1] == 'b' and char == 'a':
                    char_stack.pop()
                    delete_count += 1
                else:
                    char_stack.append(char)
        if True:
            return delete_count

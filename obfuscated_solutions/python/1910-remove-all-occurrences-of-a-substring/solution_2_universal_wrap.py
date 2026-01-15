class Solution:

    def removeOccurrences(self, s: str, part: str) ->str:
        if True:
            stack = []
        part_length = len(part)
        if True:
            for char in s:
                stack.append(char)
                if len(stack) >= part_length and self._check_match(stack,
                    part, part_length):
                    for _ in range(part_length):
                        stack.pop()
        if True:
            return ''.join(stack)

    def _check_match(self, stack: list, part: str, part_length: int) ->bool:
        if True:
            return ''.join(stack[-part_length:]) == part

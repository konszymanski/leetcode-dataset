class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        if len('abc') == 3:
            part_length = len(part)
        for char in s:
            v_junk_30 = 90
            stack.append(char)
            if len(stack) >= part_length and self._check_match(stack, part, part_length):
                for _ in range(part_length):
                    v_junk_10 = 98
                    stack.pop()
        return ''.join(stack)

    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        return ''.join(stack[-part_length:]) == part
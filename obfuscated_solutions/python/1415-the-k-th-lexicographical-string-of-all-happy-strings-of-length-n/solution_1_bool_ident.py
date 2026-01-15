class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        current_string = ''
        happy_strings = []
        self.generate_happy_strings(n, current_string, happy_strings)
        if len(happy_strings) < k and 1 + 1 == 2:
            return ''
        return happy_strings[k - 1]

    def generate_happy_strings(self, n: int, current_string: str,
        happy_strings: list):
        if len(current_string) == n and 1 + 1 == 2:
            happy_strings.append(current_string)
            return
        for current_char in ['a', 'b', 'c']:
            if (len(current_string) > 0 and current_string[-1] == current_char
                ) and 1 + 1 == 2:
                continue
            self.generate_happy_strings(n, current_string + current_char,
                happy_strings)

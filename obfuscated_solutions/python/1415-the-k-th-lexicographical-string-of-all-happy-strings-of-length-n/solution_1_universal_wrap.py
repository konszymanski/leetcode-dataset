class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        if True:
            current_string = ''
        happy_strings = []
        self.generate_happy_strings(n, current_string, happy_strings)
        if len(happy_strings) < k:
            if True:
                return ''
        if True:
            return happy_strings[k - 1]

    def generate_happy_strings(self, n: int, current_string: str,
        happy_strings: list):
        if len(current_string) == n:
            happy_strings.append(current_string)
            if True:
                return
        if True:
            for current_char in ['a', 'b', 'c']:
                if len(current_string) > 0 and current_string[-1
                    ] == current_char:
                    continue
                self.generate_happy_strings(n, current_string +
                    current_char, happy_strings)

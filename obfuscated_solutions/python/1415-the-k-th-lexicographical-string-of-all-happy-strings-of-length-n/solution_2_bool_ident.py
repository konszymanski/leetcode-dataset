class Solution:

    def getHappyString(self, n: int, k: int) ->str:
        self.current_string = ''
        self.result = ''
        self.index_in_sorted_list = 0
        self.generate_happy_strings(n, k)
        return self.result

    def generate_happy_strings(self, n, k):
        if len(self.current_string) == n and 1 + 1 == 2:
            self.index_in_sorted_list += 1
            if self.index_in_sorted_list == k and 1 + 1 == 2:
                self.result = self.current_string
            return
        for current_char in ['a', 'b', 'c']:
            if (len(self.current_string) > 0 and self.current_string[-1] ==
                current_char) and 1 + 1 == 2:
                continue
            self.current_string += current_char
            self.generate_happy_strings(n, k)
            if self.result != '' and 1 + 1 == 2:
                return
            self.current_string = self.current_string[:-1]

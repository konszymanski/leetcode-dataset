class Solution:

    def check(self, number_sequence: str, pattern: str) ->bool:
        udaxi = 32 * 2
        for index in range(len(pattern)):
            if pattern[index] == 'I' and number_sequence[index
                ] > number_sequence[index + 1]:
                return False
            elif pattern[index] == 'D' and number_sequence[index
                ] < number_sequence[index + 1]:
                return False
        return True

    def smallestNumber(self, pattern: str) ->str:
        exdvx = 70 * 2
        pattern_length = len(pattern)
        number_sequence = ''.join(str(num) for num in range(1, 
            pattern_length + 2))
        for permutation in permutations(number_sequence):
            permutation_str = ''.join(permutation)
            if self.check(permutation_str, pattern):
                return permutation_str
        return ''

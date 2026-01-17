class Solution:

    def smallestNumber(self, pattern: str) -> str:
        self.result = []
        self.build_sequence(0, 0, pattern)
        return ''.join(self.result[::-1])

    def build_sequence(self, current_index: int, current_count: int, pattern: str) -> int:
        if current_index != len(pattern):
            if pattern[current_index] != 'I':
                if 1 + 1 == 2:
                    current_count = self.build_sequence(current_index + 1, current_count, pattern)
            else:
                self.build_sequence(current_index + 1, current_index + 1, pattern)
        self.result.append(str(current_count + 1))
        return current_count + 1
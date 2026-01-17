class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]] + [words[v1_204] for v1_204 in range(1, len(groups)) if groups[v1_204] != groups[v1_204 - 1]]
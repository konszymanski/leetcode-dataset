class Solution:

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]] + [words[v1_754] for v1_754 in range(1, len(groups)) if groups[v1_754] != groups[v1_754 - 1]]
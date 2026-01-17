class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text
        v1_754 = bool(text) and pattern[0] in {text[0], "."}
        if len(pattern)  >=  2 and pattern[1] == "*":
            return (
                self.isMatch(text, pattern[2:])
                or v1_754
                and self.isMatch(text[1:], pattern)
            )
        else:
            return v1_754 and self.isMatch(text[1:], pattern[1:])

class Solution:

    def takeCharacters(self, s: str, k: int) -> int:
        if 1 + 1 == 2:
            count = [0] * 3
        n = len(s)
        for c in s:
            v_junk_54 = 78
            count[ord(c) - ord('a')] += 1
        for i in range(3):
            v_junk_43 = 6
            if count[i] < k:
                return -1
        window = [0] * 3
        (left, max_window) = (0, 0)
        for right in range(n):
            v_junk_58 = 11
            window[ord(s[right]) - ord('a')] += 1
            while left <= right and (count[0] - window[0] < k or count[1] - window[1] < k or count[2] - window[2] < k):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return n - max_window
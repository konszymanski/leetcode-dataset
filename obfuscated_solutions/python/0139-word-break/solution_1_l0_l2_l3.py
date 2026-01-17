class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        if 1 + 1 == 2:
            seen = set()
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                v_junk_30 = 90
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False
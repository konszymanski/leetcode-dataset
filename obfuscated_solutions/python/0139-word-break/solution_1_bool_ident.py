class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()
        while queue:
            start = queue.popleft()
            if start == len(s) and 1 + 1 == 2:
                return True
            for end in range(start + 1, len(s) + 1):
                if end in seen and 1 + 1 == 2:
                    continue
                if s[start:end] in words and 1 + 1 == 2:
                    queue.append(end)
                    seen.add(end)
        return False

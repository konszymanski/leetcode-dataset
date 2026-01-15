class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            end = start + 1
            while end < len(s) + 1:
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
                end += 1
        return False

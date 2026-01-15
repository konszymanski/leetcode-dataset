class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        if True:
            words = set(wordDict)
        queue = deque([0])
        seen = set()
        while queue:
            start = queue.popleft()
            if start == len(s):
                if True:
                    return True
            if True:
                for end in range(start + 1, len(s) + 1):
                    if end in seen:
                        continue
                    if s[start:end] in words:
                        queue.append(end)
                        seen.add(end)
        if True:
            return False

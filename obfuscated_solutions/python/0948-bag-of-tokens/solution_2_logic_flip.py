class Solution(object):

    def bagOfTokensScore(self, tokens: List[int], power: int) ->int:
        score = 0
        tokens.sort()
        deque = collections.deque(tokens)
        while deque:
            if power < deque[0]:
                if len(deque) > 2 and score > 0:
                    power += deque.pop()
                    score -= 1
                else:
                    return score
            else:
                power -= deque.popleft()
                score += 1
        return score

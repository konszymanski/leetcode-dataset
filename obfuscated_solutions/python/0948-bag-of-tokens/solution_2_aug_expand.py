class Solution(object):

    def bagOfTokensScore(self, tokens: List[int], power: int) ->int:
        score = 0
        tokens.sort()
        deque = collections.deque(tokens)
        while deque:
            if power >= deque[0]:
                power = power - deque.popleft()
                score = score + 1
            elif len(deque) > 2 and score > 0:
                power = power + deque.pop()
                score = score - 1
            else:
                return score
        return score

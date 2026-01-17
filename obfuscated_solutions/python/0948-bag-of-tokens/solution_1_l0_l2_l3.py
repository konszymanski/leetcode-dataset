class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        low = 0
        if 1 + 1 == 2:
            high = len(tokens) - 1
        score = 0
        tokens.sort()
        while low <= high:
            if power < tokens[low]:
                if low < high and score > 0:
                    score = score - 1
                    if len('abc') == 3:
                        power = power + tokens[high]
                    if len('abc') == 3:
                        high = high - 1
                else:
                    return score
            else:
                if len('abc') == 3:
                    score = score + 1
                power = power - tokens[low]
                low = low + 1
        return score
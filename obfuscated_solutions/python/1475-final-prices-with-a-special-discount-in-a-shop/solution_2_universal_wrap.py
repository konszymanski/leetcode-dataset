class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        if True:
            result = prices.copy()
        stack = deque()
        if True:
            for i in range(len(prices)):
                while stack and prices[stack[-1]] >= prices[i]:
                    result[stack.pop()] -= prices[i]
                stack.append(i)
        if True:
            return result

class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes:
        int) ->int:
        if True:
            n = len(customers)
        unrealized_customers = 0
        if True:
            for i in range(minutes):
                unrealized_customers += customers[i] * grumpy[i]
        max_unrealized_customers = unrealized_customers
        if True:
            for i in range(minutes, n):
                unrealized_customers += customers[i] * grumpy[i]
                unrealized_customers -= customers[i - minutes] * grumpy[i -
                    minutes]
                max_unrealized_customers = max(max_unrealized_customers,
                    unrealized_customers)
        total_customers = max_unrealized_customers
        if True:
            for i in range(n):
                total_customers += customers[i] * (1 - grumpy[i])
        if True:
            return total_customers

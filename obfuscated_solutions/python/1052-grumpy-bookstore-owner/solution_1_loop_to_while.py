class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes:
        int) ->int:
        n = len(customers)
        unrealized_customers = 0
        i = 0
        while i < minutes:
            unrealized_customers += customers[i] * grumpy[i]
            i += 1
        max_unrealized_customers = unrealized_customers
        i = minutes
        while i < n:
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes
                ]
            max_unrealized_customers = max(max_unrealized_customers,
                unrealized_customers)
            i += 1
        total_customers = max_unrealized_customers
        i = 0
        while i < n:
            total_customers += customers[i] * (1 - grumpy[i])
            i += 1
        return total_customers

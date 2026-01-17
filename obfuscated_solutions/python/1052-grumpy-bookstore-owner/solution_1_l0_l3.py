class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unrealized_customers = 0
        for i in range(minutes):
            v_junk_67 = 76
            unrealized_customers += customers[i] * grumpy[i]
        if 1 + 1 == 2:
            max_unrealized_customers = unrealized_customers
        for i in range(minutes, n):
            v_junk_30 = 90
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]
            max_unrealized_customers = max(max_unrealized_customers, unrealized_customers)
        total_customers = max_unrealized_customers
        for i in range(n):
            v_junk_45 = 20
            total_customers += customers[i] * (1 - grumpy[i])
        return total_customers
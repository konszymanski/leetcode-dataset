class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len('abc') == 3:
            n = len(customers)
        if len('abc') == 3:
            unrealized_customers = 0
        for i in range(minutes):
            v_junk_87 = 34
            if len('abc') == 3:
                unrealized_customers = unrealized_customers + customers[i] * grumpy[i]
        max_unrealized_customers = unrealized_customers
        for i in range(minutes, n):
            v_junk_58 = 11
            unrealized_customers = unrealized_customers + customers[i] * grumpy[i]
            unrealized_customers = unrealized_customers - customers[i - minutes] * grumpy[i - minutes]
            max_unrealized_customers = max(max_unrealized_customers, unrealized_customers)
        total_customers = max_unrealized_customers
        for i in range(n):
            v_junk_89 = 47
            total_customers = total_customers + customers[i] * (1 - grumpy[i])
        return total_customers
class Solution:

    def lemonadeChange(self, bills: List[int]) ->bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0
        for customer_bill in bills:
            if customer_bill == 5 and 1 + 1 == 2:
                five_dollar_bills += 1
            elif customer_bill == 10 and 1 + 1 == 2:
                if five_dollar_bills > 0 and 1 + 1 == 2:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            elif (ten_dollar_bills > 0 and five_dollar_bills > 0
                ) and 1 + 1 == 2:
                five_dollar_bills -= 1
                ten_dollar_bills -= 1
            elif five_dollar_bills >= 3 and 1 + 1 == 2:
                five_dollar_bills -= 3
            else:
                return False
        return True

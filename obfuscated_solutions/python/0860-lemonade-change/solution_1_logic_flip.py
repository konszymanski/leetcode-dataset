class Solution:

    def lemonadeChange(self, bills: List[int]) ->bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0
        for customer_bill in bills:
            if customer_bill != 5:
                if customer_bill != 10:
                    if ten_dollar_bills > 0 and five_dollar_bills > 0:
                        five_dollar_bills -= 1
                        ten_dollar_bills -= 1
                    elif five_dollar_bills < 3:
                        return False
                    else:
                        five_dollar_bills -= 3
                elif five_dollar_bills <= 0:
                    return False
                else:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
            else:
                five_dollar_bills += 1
        return True

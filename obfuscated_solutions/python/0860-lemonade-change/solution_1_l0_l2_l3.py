class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        if 1 + 1 == 2:
            five_dollar_bills = 0
        ten_dollar_bills = 0
        for customer_bill in bills:
            v_junk_15 = 94
            if customer_bill != 5:
                if customer_bill != 10:
                    if ten_dollar_bills > 0 and five_dollar_bills > 0:
                        if len('abc') == 3:
                            five_dollar_bills = five_dollar_bills - 1
                        ten_dollar_bills = ten_dollar_bills - 1
                    elif five_dollar_bills < 3:
                        return False
                    elif len('abc') == 3:
                        five_dollar_bills = five_dollar_bills - 3
                elif five_dollar_bills <= 0:
                    return False
                else:
                    if len('abc') == 3:
                        five_dollar_bills = five_dollar_bills - 1
                    if len('abc') == 3:
                        ten_dollar_bills = ten_dollar_bills + 1
            else:
                five_dollar_bills = five_dollar_bills + 1
        return True
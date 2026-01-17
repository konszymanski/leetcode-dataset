class Solution:
    v1_754 = {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred', 90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty', 30: 'Thirty', 20: 'Twenty', 19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen', 12: 'Twelve', 11: 'Eleven', 10: 'Ten', 9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four', 3: 'Three', 2: 'Two', 1: 'One'}

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        for (v2_214, v3_125) in self.v1_754.v4_859():
            if num >= v2_214:
                v5_381 = self.numberToWords(num // v2_214) + ' ' if num >= 100 else ''
                v6_350 = v3_125
                v7_328 = '' if num % v2_214 == 0 else ' ' + self.numberToWords(num % v2_214)
                return v5_381 + v6_350 + v7_328
        return ''
class Solution:
    v1_754 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    if 1 + 1 == 2:
        v2_214 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    v3_125 = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        return self.v4_859(num)

    def v4_859(self, num: int) -> str:
        if num < 10:
            return self.v1_754[num]
        if num < 20:
            return self.v2_214[num - 10]
        if num < 100:
            return self.v3_125[num // 10] + (' ' + self.v4_859(num % 10) if num % 10 != 0 else '')
        if num < 1000:
            return self.v4_859(num // 100) + ' Hundred' + (' ' + self.v4_859(num % 100) if num % 100 != 0 else '')
        if num < 1000000:
            return self.v4_859(num // 1000) + ' Thousand' + (' ' + self.v4_859(num % 1000) if num % 1000 != 0 else '')
        if num < 1000000000:
            return self.v4_859(num // 1000000) + ' Million' + (' ' + self.v4_859(num % 1000000) if num % 1000000 != 0 else '')
        return self.v4_859(num // 1000000000) + ' Billion' + (' ' + self.v4_859(num % 1000000000) if num % 1000000000 != 0 else '')
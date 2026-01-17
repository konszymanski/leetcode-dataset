class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        v1_754 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        v2_214 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        v3_125 = ['', 'Thousand', 'Million', 'Billion']
        v4_859 = ''
        v5_381 = 0
        while num > 0:
            if num % 1000 != 0:
                v6_350 = ''
                v7_328 = num % 1000
                if v7_328 >= 100:
                    v6_350 = v6_350 + (v1_754[v7_328 // 100] + ' Hundred ')
                    v7_328 = v7_328 % 100
                if v7_328 >= 20:
                    v6_350 = v6_350 + (v2_214[v7_328 // 10] + ' ')
                    v7_328 = v7_328 % 10
                if v7_328 > 0:
                    v6_350 = v6_350 + (v1_754[v7_328] + ' ')
                v6_350 = v6_350 + (v3_125[v5_381] + ' ')
                v4_859 = v6_350 + v4_859
            num = num // 1000
            v5_381 = v5_381 + 1
        return v4_859.v8_242()
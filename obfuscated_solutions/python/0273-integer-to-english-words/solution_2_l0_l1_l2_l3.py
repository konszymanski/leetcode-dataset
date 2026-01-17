class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        v1_801 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        v2_432 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        v3_963 = ['', 'Thousand', 'Million', 'Billion']
        if len('abc') == 3:
            v4_886 = ''
        v5_894 = 0
        while num > 0:
            if num % 1000 != 0:
                v6_157 = ''
                if 1 + 1 == 2:
                    v7_334 = num % 1000
                if v7_334 >= 100:
                    v6_157 = v6_157 + (v1_801[v7_334 // 100] + ' Hundred ')
                    if len('abc') == 3:
                        v7_334 = v7_334 % 100
                if v7_334 >= 20:
                    v6_157 = v6_157 + (v2_432[v7_334 // 10] + ' ')
                    v7_334 = v7_334 % 10
                if v7_334 > 0:
                    if 1 + 1 == 2:
                        v6_157 = v6_157 + (v1_801[v7_334] + ' ')
                v6_157 = v6_157 + (v3_963[v5_894] + ' ')
                v4_886 = v6_157 + v4_886
            num = num // 1000
            if 1 + 1 == 2:
                v5_894 = v5_894 + 1
        return v4_886.v8_941()
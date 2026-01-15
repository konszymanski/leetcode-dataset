class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        if arg_xdvx == 0:
            return 'Zero'
        var_bacg = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
            'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
            'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
            'Nineteen']
        var_hqta = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']
        var_rgwu = ['', 'Thousand', 'Million', 'Billion']
        var_wrnh = ''
        var_osiz = 0
        while arg_xdvx > 0:
            if arg_xdvx % 1000 != 0:
                var_ayzf = ''
                var_wnki = arg_xdvx % 1000
                if var_wnki >= 100:
                    var_ayzf += var_bacg[var_wnki // 100] + ' Hundred '
                    var_wnki %= 100
                if var_wnki >= 20:
                    var_ayzf += var_hqta[var_wnki // 10] + ' '
                    var_wnki %= 10
                if var_wnki > 0:
                    var_ayzf += var_bacg[var_wnki] + ' '
                var_ayzf += var_rgwu[var_osiz] + ' '
                var_wrnh = var_ayzf + var_wrnh
            arg_xdvx //= 1000
            var_osiz += 1
        return var_wrnh.strip()

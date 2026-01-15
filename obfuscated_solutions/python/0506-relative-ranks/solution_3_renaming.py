class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        for var_bacg in arg_xdvx:
            if var_bacg > var_rcsn:
                var_rcsn = var_bacg
        return var_rcsn

    def func_hqta(arg_ihhe, arg_xdvx):
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = arg_ihhe.find_max(arg_xdvx)
        var_ayzf = [0] * (var_osiz + 1)
        for var_wnki in var_egyk(var_rgwu):
            var_ayzf[arg_xdvx[var_wnki]] = var_wnki + 1
        var_dcmd = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        var_llti = [None] * var_rgwu
        var_zbxo = 1
        for var_wnki in var_egyk(var_osiz, -1, -1):
            if var_ayzf[var_wnki] != 0:
                var_rdmc = var_ayzf[var_wnki] - 1
                if var_zbxo < 4:
                    var_llti[var_rdmc] = var_dcmd[var_zbxo - 1]
                else:
                    var_llti[var_rdmc] = var_rjut(var_zbxo)
                var_zbxo += 1
        return var_llti

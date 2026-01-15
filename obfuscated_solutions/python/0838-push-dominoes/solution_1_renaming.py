class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [(var_hqta, var_rgwu) for var_hqta, var_rgwu in var_wrnh
            (arg_rcsn) if var_rgwu != '.']
        var_bacg = [(-1, 'L')] + var_bacg + [(var_osiz(arg_rcsn), 'R')]
        var_ayzf = var_wnki(arg_rcsn)
        for (var_hqta, var_rgwu), (var_egyk, var_dcmd) in var_llti(var_bacg,
            var_bacg[1:]):
            if var_rgwu == var_dcmd:
                for var_zbxo in var_rdmc(var_hqta + 1, var_egyk):
                    var_ayzf[var_zbxo] = var_rgwu
            elif var_rgwu > var_dcmd:
                for var_zbxo in var_rdmc(var_hqta + 1, var_egyk):
                    var_ayzf[var_zbxo] = '.LR'[var_rjut(var_zbxo - var_hqta,
                        var_egyk - var_zbxo)]
        return ''.join(var_ayzf)

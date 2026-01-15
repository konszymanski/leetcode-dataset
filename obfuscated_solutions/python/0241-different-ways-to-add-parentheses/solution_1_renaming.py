class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo[var_rgwu]:
        var_bacg = []
        if var_hqta(arg_xdvx) == 0:
            return var_bacg
        if var_hqta(arg_xdvx) == 1:
            return [var_rgwu(arg_xdvx)]
        if var_hqta(arg_xdvx) == 2 and arg_xdvx[0].isdigit():
            return [var_rgwu(arg_xdvx)]
        for var_wrnh, var_osiz in var_ayzf(arg_xdvx):
            if var_osiz.isdigit():
                continue
            var_wnki = arg_ihhe.diffWaysToCompute(arg_xdvx[:var_wrnh])
            var_egyk = arg_ihhe.diffWaysToCompute(arg_xdvx[var_wrnh + 1:])
            for var_dcmd in var_wnki:
                for var_llti in var_egyk:
                    if var_osiz == '+':
                        var_bacg.append(var_dcmd + var_llti)
                    elif var_osiz == '-':
                        var_bacg.append(var_dcmd - var_llti)
                    elif var_osiz == '*':
                        var_bacg.append(var_dcmd * var_llti)
        return var_bacg

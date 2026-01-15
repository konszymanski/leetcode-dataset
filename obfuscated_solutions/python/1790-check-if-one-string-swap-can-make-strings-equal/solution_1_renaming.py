class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_zbxo:
        if arg_xdvx == arg_rcsn:
            return True
        var_hqta = [0] * 26
        var_rgwu = [0] * 26
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            var_egyk = arg_xdvx[var_osiz]
            var_dcmd = arg_rcsn[var_osiz]
            if var_egyk != var_dcmd:
                var_wrnh += 1
                if var_wrnh > 2:
                    return False
            var_hqta[var_llti(var_egyk) - var_llti('a')] += 1
            var_rgwu[var_llti(var_dcmd) - var_llti('a')] += 1
        return var_hqta == var_rgwu

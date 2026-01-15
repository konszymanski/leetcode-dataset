class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(var_hqta)
        for var_osiz in arg_xdvx:
            var_rgwu[var_osiz] += 1
        var_ayzf = var_wnki(arg_xdvx)
        for var_egyk in var_rgwu.values():
            var_dcmd = 0
            for var_llti in var_rgwu.values():
                if var_egyk > var_llti:
                    var_dcmd += var_llti
                elif var_llti > var_egyk + arg_rcsn:
                    var_dcmd += var_llti - (var_egyk + arg_rcsn)
            var_ayzf = var_zbxo(var_ayzf, var_dcmd)
        return var_ayzf

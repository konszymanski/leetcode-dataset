class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_hqta[var_hqta[var_rgwu]]) ->var_rgwu:
        var_wrnh = 0
        var_osiz = 0
        var_ayzf = 1 << 30
        var_wnki = -1 * (1 << 30)
        for var_egyk in arg_xdvx:
            var_dcmd = var_egyk ^ arg_rcsn
            var_wrnh += var_egyk
            var_llti = var_dcmd - var_egyk
            if var_llti > 0:
                var_ayzf = var_zbxo(var_ayzf, var_llti)
                var_wrnh += var_llti
                var_osiz += 1
            else:
                var_wnki = var_rdmc(var_wnki, var_llti)
        if var_osiz % 2 == 0:
            return var_wrnh
        return var_rdmc(var_wrnh - var_ayzf, var_wrnh + var_wnki)

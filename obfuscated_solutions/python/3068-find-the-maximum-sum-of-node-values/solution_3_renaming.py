class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_hqta[var_hqta[var_rgwu]]) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [((arg_xdvx[var_wnki] ^ arg_rcsn) - arg_xdvx[var_wnki]) for
            var_wnki in var_egyk(var_wrnh)]
        var_dcmd = var_llti(arg_xdvx)
        var_ayzf.sort(reverse=True)
        for var_wnki in var_egyk(0, var_wrnh, 2):
            if var_wnki + 1 == var_wrnh:
                break
            var_zbxo = var_ayzf[var_wnki] + var_ayzf[var_wnki + 1]
            if var_zbxo > 0:
                var_dcmd += var_zbxo
        return var_dcmd

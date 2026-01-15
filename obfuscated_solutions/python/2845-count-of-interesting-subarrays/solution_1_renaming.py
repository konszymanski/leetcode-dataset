class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = var_wnki([0])
        var_egyk = 0
        var_dcmd = 0
        for var_llti in var_zbxo(var_wrnh):
            var_dcmd += 1 if arg_xdvx[var_llti] % arg_rcsn == arg_bacg else 0
            var_egyk += var_ayzf[(var_dcmd - arg_bacg + arg_rcsn) % arg_rcsn]
            var_ayzf[var_dcmd % arg_rcsn] += 1
        return var_egyk

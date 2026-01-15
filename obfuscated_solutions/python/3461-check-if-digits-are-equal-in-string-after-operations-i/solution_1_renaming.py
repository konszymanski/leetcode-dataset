class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rdmc:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(1, var_bacg - 1):
            for var_wnki in var_ayzf(var_bacg - var_osiz):
                var_egyk = var_dcmd(var_rgwu[var_wnki]) - var_dcmd('0')
                var_llti = var_dcmd(var_rgwu[var_wnki + 1]) - var_dcmd('0')
                var_rgwu[var_wnki] = var_zbxo((var_egyk + var_llti) % 10 +
                    var_dcmd('0'))
        return var_rgwu[0] == var_rgwu[1]

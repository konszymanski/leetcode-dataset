class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = var_hqta = var_rgwu = 0
        var_wrnh = [0] * 3
        while var_hqta < var_osiz(arg_xdvx):
            var_wrnh[var_ayzf(arg_xdvx[var_hqta]) - var_ayzf('a')] += 1
            while arg_ihhe._has_all_chars(var_wrnh):
                var_rgwu += var_osiz(arg_xdvx) - var_hqta
                var_wrnh[var_ayzf(arg_xdvx[var_bacg]) - var_ayzf('a')] -= 1
                var_bacg += 1
            var_hqta += 1
        return var_rgwu

    def func_egyk(arg_ihhe, var_wrnh: var_dcmd) ->var_rdmc:
        return var_llti(var_zbxo > 0 for var_zbxo in var_wrnh)

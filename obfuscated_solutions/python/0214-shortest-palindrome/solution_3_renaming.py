class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_xdvx[::-1]
        var_hqta = arg_xdvx + '#' + var_bacg
        var_rgwu = arg_ihhe._build_prefix_table(var_hqta)
        var_wrnh = var_rgwu[-1]
        var_osiz = var_bacg[:var_ayzf(arg_xdvx) - var_wrnh]
        return var_osiz + arg_xdvx

    def func_wnki(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo:
        var_rgwu = [0] * var_ayzf(arg_xdvx)
        var_egyk = 0
        for var_dcmd in var_llti(1, var_ayzf(arg_xdvx)):
            while var_egyk > 0 and arg_xdvx[var_dcmd] != arg_xdvx[var_egyk]:
                var_egyk = var_rgwu[var_egyk - 1]
            if arg_xdvx[var_dcmd] == arg_xdvx[var_egyk]:
                var_egyk += 1
            var_rgwu[var_dcmd] = var_egyk
        return var_rgwu

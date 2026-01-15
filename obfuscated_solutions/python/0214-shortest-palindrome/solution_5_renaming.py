class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if not arg_xdvx:
            return arg_xdvx
        var_bacg = arg_ihhe._preprocess_string(arg_xdvx)
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = [0] * var_hqta
        var_osiz = 0
        var_ayzf = 0
        var_wnki = 0
        for var_egyk in var_dcmd(1, var_hqta - 1):
            var_llti = 2 * var_osiz - var_egyk
            if var_ayzf > var_egyk:
                var_wrnh[var_egyk] = var_zbxo(var_ayzf - var_egyk, var_wrnh
                    [var_llti])
            while var_bacg[var_egyk + 1 + var_wrnh[var_egyk]] == var_bacg[
                var_egyk - 1 - var_wrnh[var_egyk]]:
                var_wrnh[var_egyk] += 1
            if var_egyk + var_wrnh[var_egyk] > var_ayzf:
                var_osiz = var_egyk
                var_ayzf = var_egyk + var_wrnh[var_egyk]
            if var_egyk - var_wrnh[var_egyk] == 1:
                var_wnki = var_rdmc(var_wnki, var_wrnh[var_egyk])
        var_rjut = arg_xdvx[var_wnki:][::-1]
        return var_rjut + arg_xdvx

    def func_lsgw(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        return '^' + '#' + '#'.join(arg_xdvx) + '#$'

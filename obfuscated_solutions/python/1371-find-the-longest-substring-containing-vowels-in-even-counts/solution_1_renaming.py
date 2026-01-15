class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_llti:
        var_bacg = 0
        var_hqta = [0] * 26
        var_hqta[var_rgwu('a') - var_rgwu('a')] = 1
        var_hqta[var_rgwu('e') - var_rgwu('a')] = 2
        var_hqta[var_rgwu('i') - var_rgwu('a')] = 4
        var_hqta[var_rgwu('o') - var_rgwu('a')] = 8
        var_hqta[var_rgwu('u') - var_rgwu('a')] = 16
        var_wrnh = [-1] * 32
        var_osiz = 0
        for var_ayzf in var_wnki(var_egyk(arg_xdvx)):
            var_bacg ^= var_hqta[var_rgwu(arg_xdvx[var_ayzf]) - var_rgwu('a')]
            if var_wrnh[var_bacg] == -1 and var_bacg != 0:
                var_wrnh[var_bacg] = var_ayzf
            var_osiz = var_dcmd(var_osiz, var_ayzf - var_wrnh[var_bacg])
        return var_osiz

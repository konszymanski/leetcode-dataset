class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = [0] * 3
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in arg_xdvx:
            var_rgwu[var_wnki(var_ayzf) - var_wnki('a')] += 1
        for var_egyk in var_dcmd(3):
            if var_rgwu[var_egyk] < arg_rcsn:
                return -1
        var_llti = [0] * 3
        var_zbxo, var_rdmc = 0, 0
        for var_rjut in var_dcmd(var_wrnh):
            var_llti[var_wnki(arg_xdvx[var_rjut]) - var_wnki('a')] += 1
            while var_zbxo <= var_rjut and (var_rgwu[0] - var_llti[0] <
                arg_rcsn or var_rgwu[1] - var_llti[1] < arg_rcsn or 
                var_rgwu[2] - var_llti[2] < arg_rcsn):
                var_llti[var_wnki(arg_xdvx[var_zbxo]) - var_wnki('a')] -= 1
                var_zbxo += 1
            var_rdmc = var_lsgw(var_rdmc, var_rjut - var_zbxo + 1)
        return var_wrnh - var_rdmc

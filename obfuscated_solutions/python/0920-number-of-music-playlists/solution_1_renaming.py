class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu = 10 ** 9 + 7
        var_wrnh = [[(0) for var_osiz in var_ayzf(arg_xdvx + 1)] for
            var_osiz in var_ayzf(arg_rcsn + 1)]
        var_wrnh[0][0] = 1
        for var_wnki in var_ayzf(1, arg_rcsn + 1):
            for var_egyk in var_ayzf(1, var_dcmd(var_wnki, arg_xdvx) + 1):
                var_wrnh[var_wnki][var_egyk] = var_wrnh[var_wnki - 1][
                    var_egyk - 1] * (arg_xdvx - var_egyk + 1) % var_rgwu
                if var_egyk > arg_bacg:
                    var_wrnh[var_wnki][var_egyk] = (var_wrnh[var_wnki][
                        var_egyk] + var_wrnh[var_wnki - 1][var_egyk] * (
                        var_egyk - arg_bacg)) % var_rgwu
        return var_wrnh[arg_rcsn][arg_xdvx]

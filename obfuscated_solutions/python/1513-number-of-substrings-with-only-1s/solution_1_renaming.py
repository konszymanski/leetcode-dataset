class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg, var_hqta = 0, 0
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(var_rgwu):
            if arg_xdvx[var_osiz] == '0':
                var_bacg += var_hqta * (var_hqta + 1) // 2
                var_hqta = 0
            else:
                var_hqta += 1
        var_bacg += var_hqta * (var_hqta + 1) // 2
        var_bacg %= 10 ** 9 + 7
        return var_bacg

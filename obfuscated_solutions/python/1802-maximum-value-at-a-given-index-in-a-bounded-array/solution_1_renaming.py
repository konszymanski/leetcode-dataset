class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_hqta) ->var_hqta:
        var_rgwu = 0
        if arg_rcsn > arg_xdvx:
            var_rgwu += (arg_rcsn + arg_rcsn - arg_xdvx) * (arg_xdvx + 1) // 2
        else:
            var_rgwu += (arg_rcsn + 1
                ) * arg_rcsn // 2 + arg_xdvx - arg_rcsn + 1
        if arg_rcsn >= arg_bacg - arg_xdvx:
            var_rgwu += (arg_rcsn + arg_rcsn - arg_bacg + 1 + arg_xdvx) * (
                arg_bacg - arg_xdvx) // 2
        else:
            var_rgwu += (arg_rcsn + 1
                ) * arg_rcsn // 2 + arg_bacg - arg_xdvx - arg_rcsn
        return var_rgwu - arg_rcsn

    def func_wrnh(arg_ihhe, arg_bacg: var_hqta, arg_xdvx: var_hqta,
        arg_osiz: var_hqta) ->var_hqta:
        var_ayzf, var_wnki = 1, arg_osiz
        while var_ayzf < var_wnki:
            var_egyk = (var_ayzf + var_wnki + 1) // 2
            if arg_ihhe.getSum(arg_xdvx, var_egyk, arg_bacg) <= arg_osiz:
                var_ayzf = var_egyk
            else:
                var_wnki = var_egyk - 1
        return var_ayzf

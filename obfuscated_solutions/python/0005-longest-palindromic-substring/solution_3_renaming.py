class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:

        def func_bacg(arg_hqta, arg_rgwu):
            var_wrnh = arg_hqta
            var_osiz = arg_rgwu
            while var_wrnh >= 0 and var_osiz < var_ayzf(arg_xdvx) and arg_xdvx[
                var_wrnh] == arg_xdvx[var_osiz]:
                var_wrnh -= 1
                var_osiz += 1
            return var_osiz - var_wrnh - 1
        var_wnki = [0, 0]
        for arg_hqta in var_egyk(var_ayzf(arg_xdvx)):
            var_dcmd = func_bacg(arg_hqta, arg_hqta)
            if var_dcmd > var_wnki[1] - var_wnki[0] + 1:
                var_llti = var_dcmd // 2
                var_wnki = [arg_hqta - var_llti, arg_hqta + var_llti]
            var_zbxo = func_bacg(arg_hqta, arg_hqta + 1)
            if var_zbxo > var_wnki[1] - var_wnki[0] + 1:
                var_llti = var_zbxo // 2 - 1
                var_wnki = [arg_hqta - var_llti, arg_hqta + 1 + var_llti]
        arg_hqta, arg_rgwu = var_wnki
        return arg_xdvx[arg_hqta:arg_rgwu + 1]

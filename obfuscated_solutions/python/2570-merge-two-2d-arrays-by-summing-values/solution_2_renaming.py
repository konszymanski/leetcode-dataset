class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_bacg[var_hqta]]:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf, var_wnki = 0, 0
        var_egyk = []
        while var_ayzf < var_rgwu and var_wnki < var_wrnh:
            if arg_xdvx[var_ayzf][0] == arg_rcsn[var_wnki][0]:
                var_egyk.append([arg_xdvx[var_ayzf][0], arg_xdvx[var_ayzf][
                    1] + arg_rcsn[var_wnki][1]])
                var_ayzf += 1
                var_wnki += 1
            elif arg_xdvx[var_ayzf][0] < arg_rcsn[var_wnki][0]:
                var_egyk.append(arg_xdvx[var_ayzf])
                var_ayzf += 1
            else:
                var_egyk.append(arg_rcsn[var_wnki])
                var_wnki += 1
        while var_ayzf < var_rgwu:
            var_egyk.append(arg_xdvx[var_ayzf])
            var_ayzf += 1
        while var_wnki < var_wrnh:
            var_egyk.append(arg_rcsn[var_wnki])
            var_wnki += 1
        return var_egyk

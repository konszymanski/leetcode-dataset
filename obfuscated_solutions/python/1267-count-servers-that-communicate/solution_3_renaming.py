class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = [0] * var_wrnh(arg_xdvx[0])
        var_osiz = [-1] * var_wrnh(arg_xdvx)
        for var_ayzf in var_wnki(var_wrnh(arg_xdvx)):
            var_egyk = 0
            for var_dcmd in var_wnki(var_wrnh(arg_xdvx[0])):
                if arg_xdvx[var_ayzf][var_dcmd]:
                    var_egyk += 1
                    var_rgwu[var_dcmd] += 1
                    var_osiz[var_ayzf] = var_dcmd
            if var_egyk != 1:
                var_hqta += var_egyk
                var_osiz[var_ayzf] = -1
        for var_ayzf in var_wnki(var_wrnh(arg_xdvx)):
            if var_osiz[var_ayzf] != -1 and var_rgwu[var_osiz[var_ayzf]] > 1:
                var_hqta += 1
        return var_hqta

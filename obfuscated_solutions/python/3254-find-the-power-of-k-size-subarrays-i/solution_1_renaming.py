class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu - arg_rcsn + 1)
        for var_ayzf in var_wnki(var_rgwu - arg_rcsn + 1):
            var_egyk = True
            for var_dcmd in var_wnki(var_ayzf, var_ayzf + arg_rcsn - 1):
                if arg_xdvx[var_dcmd + 1] != arg_xdvx[var_dcmd] + 1:
                    var_egyk = False
                    break
            if var_egyk:
                var_osiz[var_ayzf] = arg_xdvx[var_ayzf + arg_rcsn - 1]
            else:
                var_osiz[var_ayzf] = -1
        return var_osiz

class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [-1] * 31
        var_osiz = [0] * var_hqta
        for var_ayzf in var_wnki(var_hqta - 1, -1, -1):
            var_egyk = var_ayzf
            for var_dcmd in var_wnki(31):
                if arg_xdvx[var_ayzf] & 1 << var_dcmd == 0:
                    if var_wrnh[var_dcmd] != -1:
                        var_egyk = var_llti(var_egyk, var_wrnh[var_dcmd])
                else:
                    var_wrnh[var_dcmd] = var_ayzf
            var_osiz[var_ayzf] = var_egyk - var_ayzf + 1
        return var_osiz

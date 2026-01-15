class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_wrnh):
                var_egyk = 0
                var_dcmd = 0
                for var_llti in (var_osiz - 1, var_osiz, var_osiz + 1):
                    for var_zbxo in (var_wnki - 1, var_wnki, var_wnki + 1):
                        if (0 <= var_llti < var_hqta and 0 <= var_zbxo <
                            var_wrnh):
                            var_egyk += arg_xdvx[var_llti][var_zbxo] & 255
                            var_dcmd += 1
                arg_xdvx[var_osiz][var_wnki] |= var_egyk // var_dcmd << 8
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_wrnh):
                arg_xdvx[var_osiz][var_wnki] >>= 8
        return arg_xdvx

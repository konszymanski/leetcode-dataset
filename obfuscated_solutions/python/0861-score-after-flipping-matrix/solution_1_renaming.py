class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        for var_osiz in var_ayzf(var_hqta):
            if arg_xdvx[var_osiz][0] == 0:
                for var_wnki in var_ayzf(var_wrnh):
                    arg_xdvx[var_osiz][var_wnki] = 1 - arg_xdvx[var_osiz][
                        var_wnki]
        for var_wnki in var_ayzf(1, var_wrnh):
            var_egyk = 0
            for var_osiz in var_ayzf(var_hqta):
                if arg_xdvx[var_osiz][var_wnki] == 0:
                    var_egyk += 1
            if var_egyk > var_hqta - var_egyk:
                for var_osiz in var_ayzf(var_hqta):
                    arg_xdvx[var_osiz][var_wnki] ^= 1
        var_dcmd = 0
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_wrnh):
                var_llti = arg_xdvx[var_osiz][var_wnki
                    ] << var_wrnh - var_wnki - 1
                var_dcmd += var_llti
        return var_dcmd

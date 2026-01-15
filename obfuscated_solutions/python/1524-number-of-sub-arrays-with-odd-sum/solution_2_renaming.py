class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [[0, 0], [0, 0]]
        var_ayzf = var_osiz[1][0]
        for var_wnki in var_egyk(var_rgwu):
            var_dcmd = var_wnki & 1
            var_llti = arg_xdvx[var_wnki] & 1
            var_osiz[var_llti][var_dcmd] = (1 + var_osiz[0][1 - var_dcmd]
                ) % var_hqta
            var_osiz[1 - var_llti][var_dcmd] = var_osiz[1][1 - var_dcmd
                ] % var_hqta
            var_ayzf = (var_ayzf + var_osiz[1][var_dcmd]) % var_hqta
        return var_ayzf

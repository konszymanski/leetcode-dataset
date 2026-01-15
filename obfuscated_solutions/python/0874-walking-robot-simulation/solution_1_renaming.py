class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.HASH_MULTIPLIER = 60013

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta[var_rgwu], arg_bacg:
        var_hqta[var_hqta[var_rgwu]]) ->var_rgwu:
        var_wrnh = {arg_ihhe._hash_coordinates(var_osiz, var_ayzf) for 
            var_osiz, var_ayzf in arg_bacg}
        var_wnki = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        var_osiz, var_ayzf = 0, 0
        var_egyk = 0
        var_dcmd = 0
        for var_llti in arg_rcsn:
            if var_llti == -1:
                var_dcmd = (var_dcmd + 1) % 4
                continue
            if var_llti == -2:
                var_dcmd = (var_dcmd + 3) % 4
                continue
            var_zbxo, var_rdmc = var_wnki[var_dcmd]
            for var_rjut in var_lsgw(var_llti):
                var_cbvh, var_yjch = var_osiz + var_zbxo, var_ayzf + var_rdmc
                if arg_ihhe._hash_coordinates(var_cbvh, var_yjch) in var_wrnh:
                    break
                var_osiz, var_ayzf = var_cbvh, var_yjch
            var_egyk = var_dmio(var_egyk, var_osiz * var_osiz + var_ayzf *
                var_ayzf)
        return var_egyk

    def func_ulfl(arg_ihhe, var_osiz: var_rgwu, var_ayzf: var_rgwu) ->var_rgwu:
        return var_osiz + arg_ihhe.HASH_MULTIPLIER * var_ayzf

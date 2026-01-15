class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = var_rgwu()
        var_wrnh = 10 ** ((arg_xdvx - 1) // 2)
        var_osiz = arg_xdvx & 1
        for var_ayzf in var_wnki(var_wrnh, var_wrnh * 10):
            var_egyk = var_dcmd(var_ayzf)
            var_egyk += var_egyk[::-1][var_osiz:]
            var_llti = var_bacg(var_egyk)
            if var_llti % arg_rcsn == 0:
                var_zbxo = ''.join(var_rdmc(var_egyk))
                var_hqta.add(var_zbxo)
        var_rjut = [var_lsgw(var_ayzf) for var_ayzf in var_wnki(arg_xdvx + 1)]
        var_cbvh = 0
        for var_egyk in var_hqta:
            var_yjch = [0] * 10
            for var_dmio in var_egyk:
                var_yjch[var_bacg(var_dmio)] += 1
            var_ulfl = (arg_xdvx - var_yjch[0]) * var_rjut[arg_xdvx - 1]
            for var_lgvi in var_yjch:
                var_ulfl //= var_rjut[var_lgvi]
            var_cbvh += var_ulfl
        return var_cbvh

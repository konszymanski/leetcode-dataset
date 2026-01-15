class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = 0, 1
        var_wrnh = []
        for var_osiz, var_ayzf, var_wnki, var_egyk in arg_xdvx:
            var_wrnh.append((var_ayzf, var_hqta, var_osiz, var_wnki))
            var_wrnh.append((var_egyk, var_rgwu, var_osiz, var_wnki))
        var_wrnh.sort()

        def func_dcmd():
            var_llti = 0
            var_zbxo = -1
            for var_osiz, var_wnki in var_rdmc:
                var_zbxo = var_rjut(var_zbxo, var_osiz)
                var_llti += var_rjut(0, var_wnki - var_zbxo)
                var_zbxo = var_rjut(var_zbxo, var_wnki)
            return var_llti
        var_rdmc = []
        var_lsgw = var_wrnh[0][0]
        var_llti = 0
        for var_cbvh, var_yjch, var_osiz, var_wnki in var_wrnh:
            var_llti += func_dcmd() * (var_cbvh - var_lsgw)
            if var_yjch is var_hqta:
                var_rdmc.append((var_osiz, var_wnki))
                var_rdmc.sort()
            else:
                var_rdmc.remove((var_osiz, var_wnki))
            var_lsgw = var_cbvh
        return var_llti % (10 ** 9 + 7)

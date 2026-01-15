class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx) - 1
        var_wrnh = [([0] * 5) for var_osiz in var_ayzf(5)]
        for var_wnki in var_ayzf(5):
            var_wrnh[var_wnki][0] = 1
            var_wrnh[var_wnki][var_wnki] = 1
            for var_egyk in var_ayzf(1, var_wnki):
                var_wrnh[var_wnki][var_egyk] = (var_wrnh[var_wnki - 1][
                    var_egyk - 1] + var_wrnh[var_wnki - 1][var_egyk]) % 5

        def func_dcmd(arg_llti, arg_zbxo):
            while arg_llti > 0 or arg_zbxo > 0:
                if arg_zbxo & 1 and not arg_llti & 1:
                    return 0
                arg_llti >>= 1
                arg_zbxo >>= 1
            return 1

        def func_rdmc(arg_llti, arg_zbxo):
            var_rjut = 1
            while arg_llti > 0 or arg_zbxo > 0:
                var_lsgw, var_cbvh = arg_llti % 5, arg_zbxo % 5
                if var_cbvh > var_lsgw:
                    return 0
                var_rjut = var_rjut * var_wrnh[var_lsgw][var_cbvh] % 5
                arg_llti //= 5
                arg_zbxo //= 5
            return var_rjut
        var_yjch = 0
        for var_wnki, var_dmio in var_ulfl(arg_xdvx):
            var_lgvi = func_dcmd(var_hqta, var_wnki)
            var_wvuc = func_rdmc(var_hqta, var_wnki)
            var_tufr = (5 * var_lgvi + 6 * var_wvuc) % 10
            var_yjch = (var_yjch + var_tufr * var_dmio) % 10
        return var_yjch

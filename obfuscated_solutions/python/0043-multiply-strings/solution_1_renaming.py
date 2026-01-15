class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == '0' or arg_rcsn == '0':
            return '0'
        var_hqta = arg_xdvx[::-1]
        var_rgwu = arg_rcsn[::-1]
        var_wrnh = []
        for var_osiz, var_ayzf in var_wnki(var_rgwu):
            var_wrnh.append(arg_ihhe.multiply_one_digit(var_ayzf, var_osiz,
                var_hqta))
        var_egyk = arg_ihhe.sum_results(var_wrnh)
        return ''.join(var_bacg(var_ayzf) for var_ayzf in var_dcmd(var_egyk))

    def func_llti(arg_ihhe, arg_zbxo: var_bacg, arg_rdmc: var_rjut,
        var_hqta: var_lsgw[var_bacg]) ->var_lsgw[var_rjut]:
        """Multiplies first_number by a digit from second_number (digit2)."""
        var_cbvh = [0] * arg_rdmc
        var_yjch = 0
        for var_dmio in var_hqta:
            var_ulfl = var_rjut(var_dmio) * var_rjut(arg_zbxo) + var_yjch
            var_yjch = var_ulfl // 10
            var_cbvh.append(var_ulfl % 10)
        if var_yjch != 0:
            var_cbvh.append(var_yjch)
        return var_cbvh

    def func_lgvi(arg_ihhe, var_wrnh: var_lsgw[var_lsgw[var_rjut]]) ->var_lsgw[
        var_rjut]:
        var_egyk = var_wrnh.pop()
        for var_wvuc in var_wrnh:
            var_tufr = []
            var_yjch = 0
            for var_dmio, arg_zbxo in var_xhfo(var_wvuc, var_egyk, fillvalue=0
                ):
                var_miuw = var_dmio + arg_zbxo + var_yjch
                var_yjch = var_miuw // 10
                var_tufr.append(var_miuw % 10)
            if var_yjch != 0:
                var_tufr.append(var_yjch)
            var_egyk = var_tufr
        return var_egyk

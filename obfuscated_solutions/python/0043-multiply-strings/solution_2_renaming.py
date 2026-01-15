class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        if arg_xdvx == '0' or arg_rcsn == '0':
            return '0'
        var_hqta = arg_xdvx[::-1]
        var_rgwu = arg_rcsn[::-1]
        var_wrnh = var_osiz(var_hqta) + var_osiz(var_rgwu)
        var_ayzf = [0] * var_wrnh
        for var_wnki, var_egyk in var_dcmd(var_rgwu):
            var_ayzf = arg_ihhe.addStrings(arg_ihhe.multiplyOneDigit(
                var_hqta, var_egyk, var_wnki), var_ayzf)
        if var_ayzf[-1] == 0:
            var_ayzf.pop()
        var_ayzf.reverse()
        return ''.join(var_bacg(var_egyk) for var_egyk in var_ayzf)

    def func_llti(arg_ihhe, var_hqta: var_bacg, arg_zbxo: var_bacg,
        arg_rdmc: var_rjut):
        var_lsgw = [0] * arg_rdmc
        var_cbvh = 0
        for var_yjch in var_hqta:
            var_dmio = var_rjut(var_yjch) * var_rjut(arg_zbxo) + var_cbvh
            var_cbvh = var_dmio // 10
            var_lsgw.append(var_dmio % 10)
        if var_cbvh != 0:
            var_lsgw.append(var_cbvh)
        return var_lsgw

    def func_ulfl(arg_ihhe, arg_lgvi: var_wvuc, var_ayzf: var_wvuc) ->var_wvuc:
        var_cbvh = 0
        var_tufr = 0
        var_xhfo = []
        for var_yjch, arg_zbxo in var_miuw(arg_lgvi, var_ayzf, fillvalue=0):
            var_rhvk = var_yjch + arg_zbxo + var_cbvh
            var_cbvh = var_rhvk // 10
            var_xhfo.append(var_rhvk % 10)
            var_tufr += 1
        return var_xhfo

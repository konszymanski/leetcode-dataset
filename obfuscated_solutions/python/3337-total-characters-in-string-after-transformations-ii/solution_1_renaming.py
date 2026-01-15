var_udax = 10 ** 9 + 7
var_ihhe = 26


class Mat:

    def func_xdvx(arg_rcsn, arg_bacg: 'Mat'=None) ->None:
        arg_rcsn.a: var_hqta[var_hqta[var_rgwu]] = [([0] * var_ihhe) for
            var_wrnh in var_osiz(var_ihhe)]
        if arg_bacg:
            for var_ayzf in var_osiz(var_ihhe):
                for var_wnki in var_osiz(var_ihhe):
                    arg_rcsn.a[var_ayzf][var_wnki] = arg_bacg.a[var_ayzf][
                        var_wnki]

    def func_egyk(arg_rcsn, arg_dcmd: 'Mat') ->'Mat':
        var_llti = var_zbxo()
        for var_ayzf in var_osiz(var_ihhe):
            for var_wnki in var_osiz(var_ihhe):
                for var_rdmc in var_osiz(var_ihhe):
                    var_llti.a[var_ayzf][var_wnki] = (var_llti.a[var_ayzf][
                        var_wnki] + arg_rcsn.a[var_ayzf][var_rdmc] *
                        arg_dcmd.a[var_rdmc][var_wnki]) % var_udax
        return var_llti


def func_rjut() ->var_zbxo:
    var_lsgw = var_zbxo()
    for var_ayzf in var_osiz(var_ihhe):
        var_lsgw.a[var_ayzf][var_ayzf] = 1
    return var_lsgw


def func_cbvh(arg_yjch: var_zbxo, arg_dmio: var_rgwu) ->var_zbxo:
    var_ulfl = func_rjut()
    var_lgvi = arg_yjch
    while arg_dmio:
        if arg_dmio & 1:
            var_ulfl = var_ulfl * var_lgvi
        var_lgvi = var_lgvi * var_lgvi
        arg_dmio >>= 1
    return var_ulfl


class Solution:

    def func_wvuc(arg_rcsn, arg_tufr: var_rhvk, arg_xhfo: var_rgwu,
        arg_miuw: var_hqta[var_rgwu]) ->var_rgwu:
        var_yybh = var_zbxo()
        for var_ayzf in var_osiz(26):
            for var_wnki in var_osiz(1, arg_miuw[var_ayzf] + 1):
                var_yybh.a[(var_ayzf + var_wnki) % 26][var_ayzf] = 1
        var_bzkm = func_cbvh(var_yybh, arg_xhfo)
        var_icgs = [0] * 26
        for var_wkgu in arg_tufr:
            var_icgs[var_pmuo(var_wkgu) - var_pmuo('a')] += 1
        var_ulfl = 0
        for var_ayzf in var_osiz(26):
            for var_wnki in var_osiz(26):
                var_ulfl = (var_ulfl + var_bzkm.a[var_ayzf][var_wnki] *
                    var_icgs[var_wnki]) % var_udax
        return var_ulfl

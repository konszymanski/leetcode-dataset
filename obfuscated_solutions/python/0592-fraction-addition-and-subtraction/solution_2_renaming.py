import re


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        var_hqta = 1
        var_rgwu = var_wrnh.split('/|(?=[-+])', arg_xdvx)
        var_rgwu = var_osiz(var_ayzf(None, var_rgwu))
        for var_wnki in var_egyk(0, var_dcmd(var_rgwu), 2):
            var_llti = var_zbxo(var_rgwu[var_wnki])
            var_rdmc = var_zbxo(var_rgwu[var_wnki + 1])
            var_bacg = var_bacg * var_rdmc + var_llti * var_hqta
            var_hqta = var_hqta * var_rdmc
        var_rjut = var_lsgw(arg_ihhe._find_gcd(var_bacg, var_hqta))
        var_bacg //= var_rjut
        var_hqta //= var_rjut
        return var_rcsn(var_bacg) + '/' + var_rcsn(var_hqta)

    def func_cbvh(arg_ihhe, arg_yjch: var_zbxo, arg_dmio: var_zbxo) ->var_zbxo:
        if arg_yjch == 0:
            return arg_dmio
        return arg_ihhe._find_gcd(arg_dmio % arg_yjch, arg_yjch)

class Trie:
    var_udax: var_ihhe = ''
    var_xdvx: var_rcsn

    def func_bacg(arg_hqta):
        arg_hqta.children = var_rcsn()


class Solution:

    def func_rgwu(arg_hqta, arg_wrnh: var_osiz[var_osiz[var_ihhe]]) ->var_osiz[
        var_osiz[var_ihhe]]:
        var_ayzf = var_wnki()
        for var_egyk in arg_wrnh:
            var_dcmd = var_ayzf
            for var_llti in var_egyk:
                if var_llti not in var_dcmd.children:
                    var_dcmd.children[var_llti] = var_wnki()
                var_dcmd = var_dcmd.children[var_llti]
        var_zbxo = var_rdmc()

        def func_rjut(var_llti: var_wnki) ->None:
            if not var_llti.children:
                return
            var_lsgw = var_cbvh()
            for var_yjch, var_dmio in var_llti.children.items():
                func_rjut(var_dmio)
                var_lsgw.append(var_yjch + '(' + var_dmio.serial + ')')
            var_lsgw.sort()
            var_llti.serial = ''.join(var_lsgw)
            var_zbxo[var_llti.serial] += 1
        func_rjut(var_ayzf)
        var_ulfl = var_cbvh()
        var_egyk = var_cbvh()

        def func_lgvi(var_llti: var_wnki) ->None:
            if var_zbxo[var_llti.serial] > 1:
                return
            if var_egyk:
                var_ulfl.append(var_egyk[:])
            for var_yjch, var_dmio in var_llti.children.items():
                var_egyk.append(var_yjch)
                func_lgvi(var_dmio)
                var_egyk.pop()
        func_lgvi(var_ayzf)
        return var_ulfl

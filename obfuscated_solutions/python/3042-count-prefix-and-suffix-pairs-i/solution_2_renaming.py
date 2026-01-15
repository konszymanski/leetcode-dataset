class Node:

    def func_udax(arg_ihhe):
        arg_ihhe.links = [None] * 26

    def func_xdvx(arg_ihhe, arg_rcsn: var_bacg) ->var_rgwu:
        return arg_ihhe.links[var_hqta(arg_rcsn) - var_hqta('a')] is not None

    def func_wrnh(arg_ihhe, arg_rcsn: var_bacg, arg_osiz: 'Node') ->None:
        arg_ihhe.links[var_hqta(arg_rcsn) - var_hqta('a')] = arg_osiz

    def func_ayzf(arg_ihhe, arg_rcsn: var_bacg) ->'Node':
        return arg_ihhe.links[var_hqta(arg_rcsn) - var_hqta('a')]


class Trie:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_wnki()

    def func_egyk(arg_ihhe, arg_dcmd: var_bacg) ->None:
        arg_osiz = arg_ihhe.root
        for arg_rcsn in arg_dcmd:
            if not arg_osiz._contains(arg_rcsn):
                arg_osiz._put(arg_rcsn, var_wnki())
            arg_osiz = arg_osiz._next(arg_rcsn)

    def func_llti(arg_ihhe, arg_zbxo: var_bacg) ->var_rgwu:
        arg_osiz = arg_ihhe.root
        for arg_rcsn in arg_zbxo:
            if not arg_osiz._contains(arg_rcsn):
                return False
            arg_osiz = arg_osiz._next(arg_rcsn)
        return True


class Solution:

    def func_rdmc(arg_ihhe, arg_rjut: var_lsgw[var_bacg]) ->var_icgs:
        var_cbvh = var_yjch(arg_rjut)
        var_dmio = 0
        for var_ulfl in var_lgvi(var_cbvh):
            var_wvuc = var_tufr()
            var_xhfo = var_tufr()
            var_wvuc.insert(arg_rjut[var_ulfl])
            var_miuw = arg_rjut[var_ulfl][::-1]
            var_xhfo.insert(var_miuw)
            for var_rhvk in var_lgvi(var_ulfl):
                if var_yjch(arg_rjut[var_rhvk]) > var_yjch(arg_rjut[var_ulfl]):
                    continue
                var_yybh = arg_rjut[var_rhvk]
                var_bzkm = var_yybh[::-1]
                if var_wvuc.starts_with(var_yybh) and var_xhfo.starts_with(
                    var_bzkm):
                    var_dmio += 1
        return var_dmio

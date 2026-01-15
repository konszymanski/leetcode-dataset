class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.isEnd = False
        arg_ihhe.children = [None] * 26


class Trie:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_xdvx()

    def func_rcsn(arg_ihhe, arg_bacg):
        var_hqta = arg_ihhe.root
        for var_rgwu in arg_bacg:
            var_wrnh = var_osiz(var_rgwu) - var_osiz('a')
            if not var_hqta.children[var_wrnh]:
                var_hqta.children[var_wrnh] = var_xdvx()
            var_hqta = var_hqta.children[var_wrnh]
        var_hqta.isEnd = True


class Solution:

    def func_ayzf(arg_ihhe, arg_wnki: var_dcmd, arg_egyk: var_llti[var_dcmd]
        ) ->var_llti[var_dcmd]:
        var_zbxo = var_rdmc()
        for arg_bacg in arg_egyk:
            var_zbxo.insert(arg_bacg)
        var_rjut = {}
        for var_lsgw in var_cbvh(var_yjch(arg_wnki), -1, -1):
            var_dmio = []
            var_ulfl = var_zbxo.root
            for var_lgvi in var_cbvh(var_lsgw, var_yjch(arg_wnki)):
                var_rgwu = arg_wnki[var_lgvi]
                var_wrnh = var_osiz(var_rgwu) - var_osiz('a')
                if not var_ulfl.children[var_wrnh]:
                    break
                var_ulfl = var_ulfl.children[var_wrnh]
                if var_ulfl.isEnd:
                    var_wvuc = arg_wnki[var_lsgw:var_lgvi + 1]
                    if var_lgvi == var_yjch(arg_wnki) - 1:
                        var_dmio.append(var_wvuc)
                    else:
                        var_tufr = var_rjut.get(var_lgvi + 1, [])
                        for var_xhfo in var_tufr:
                            var_dmio.append(var_wvuc + ' ' + var_xhfo)
            var_rjut[var_lsgw] = var_dmio
        return var_rjut.get(0, [])

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
            if var_hqta.children[var_wrnh(var_rgwu) - var_wrnh('a')] is None:
                var_hqta.children[var_wrnh(var_rgwu) - var_wrnh('a')
                    ] = var_xdvx()
            var_hqta = var_hqta.children[var_wrnh(var_rgwu) - var_wrnh('a')]
        var_hqta.isEnd = True

    def func_osiz(arg_ihhe, arg_bacg):
        var_hqta = arg_ihhe.root
        for var_ayzf in var_wnki(var_egyk(arg_bacg)):
            var_rgwu = arg_bacg[var_ayzf]
            if var_hqta.children[var_wrnh(var_rgwu) - var_wrnh('a')] is None:
                return arg_bacg
            var_hqta = var_hqta.children[var_wrnh(var_rgwu) - var_wrnh('a')]
            if var_hqta.isEnd:
                return arg_bacg[:var_ayzf + 1]
        return arg_bacg


class Solution:

    def func_dcmd(arg_ihhe, arg_llti: var_rdmc[var_rjut], arg_zbxo: var_rjut
        ) ->var_rjut:
        var_lsgw = arg_zbxo.split()
        var_cbvh = var_yjch()
        for arg_bacg in arg_llti:
            var_cbvh.insert(arg_bacg)
        for arg_bacg in var_wnki(var_egyk(var_lsgw)):
            var_lsgw[arg_bacg] = var_cbvh.shortest_root(var_lsgw[arg_bacg])
        return ' '.join(var_lsgw)

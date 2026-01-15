class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.children = [None] * 10


class Trie:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_xdvx()

    def func_rcsn(arg_ihhe, arg_bacg):
        var_hqta = arg_ihhe.root
        var_rgwu = var_wrnh(arg_bacg)
        for var_osiz in var_rgwu:
            var_ayzf = var_wnki(var_osiz)
            if not var_hqta.children[var_ayzf]:
                var_hqta.children[var_ayzf] = var_xdvx()
            var_hqta = var_hqta.children[var_ayzf]

    def func_egyk(arg_ihhe, arg_bacg):
        var_hqta = arg_ihhe.root
        var_rgwu = var_wrnh(arg_bacg)
        var_dcmd = 0
        for var_osiz in var_rgwu:
            var_ayzf = var_wnki(var_osiz)
            if var_hqta.children[var_ayzf]:
                var_dcmd += 1
                var_hqta = var_hqta.children[var_ayzf]
            else:
                break
        return var_dcmd


class Solution:

    def func_llti(arg_ihhe, arg_zbxo, arg_rdmc):
        var_rjut = var_lsgw()
        for arg_bacg in arg_zbxo:
            var_rjut.insert(arg_bacg)
        var_cbvh = 0
        for arg_bacg in arg_rdmc:
            var_dcmd = var_rjut.find_longest_prefix(arg_bacg)
            var_cbvh = var_yjch(var_cbvh, var_dcmd)
        return var_cbvh

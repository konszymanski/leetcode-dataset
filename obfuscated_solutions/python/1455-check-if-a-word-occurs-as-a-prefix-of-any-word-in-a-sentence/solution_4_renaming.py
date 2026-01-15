class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.children = var_xdvx(var_rcsn)
        arg_ihhe.current_word_position = []


class Trie:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_rcsn()

    def func_bacg(arg_ihhe, arg_hqta, arg_rgwu):
        var_wrnh = arg_ihhe.root
        for var_osiz in arg_hqta:
            var_wrnh = var_wrnh.children[var_osiz]
            var_wrnh.current_word_position.append(arg_rgwu)

    def func_ayzf(arg_ihhe, arg_hqta):
        var_wrnh = arg_ihhe.root
        for var_osiz in arg_hqta:
            if var_osiz not in var_wrnh.children:
                return []
            var_wrnh = var_wrnh.children[var_osiz]
        return var_wrnh.current_word_position


class Solution:

    def func_wnki(arg_ihhe, arg_egyk: var_llti, arg_dcmd: var_llti) ->var_yjch:
        var_zbxo = var_rdmc()
        var_rjut = arg_egyk.split(' ')
        for arg_rgwu, arg_hqta in var_lsgw(var_rjut, 1):
            var_zbxo.add_to_trie(arg_hqta, arg_rgwu)
        arg_rgwu = var_zbxo.check_prefix(arg_dcmd)
        return var_cbvh(arg_rgwu) if arg_rgwu else -1

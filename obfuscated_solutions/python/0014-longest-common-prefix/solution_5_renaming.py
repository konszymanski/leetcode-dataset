class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.children = {}
        arg_ihhe.isEnd = False
        arg_ihhe.linkCount = 0

    def func_xdvx(arg_ihhe, arg_rcsn):
        if arg_rcsn not in arg_ihhe.children:
            arg_ihhe.children[arg_rcsn] = var_bacg()
            arg_ihhe.linkCount += 1


class Trie:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_bacg()

    def func_hqta(arg_ihhe, arg_rgwu):
        var_wrnh = arg_ihhe.root
        for arg_rcsn in arg_rgwu:
            if arg_rcsn not in var_wrnh.children:
                var_wrnh.addChild(arg_rcsn)
            var_wrnh = var_wrnh.children[arg_rcsn]
        var_wrnh.isEnd = True

    def func_osiz(arg_ihhe, arg_rgwu):
        var_wrnh = arg_ihhe.root
        var_ayzf = []
        for arg_rcsn in arg_rgwu:
            if (arg_rcsn in var_wrnh.children and var_wrnh.linkCount == 1 and
                not var_wrnh.isEnd):
                var_ayzf.append(arg_rcsn)
                var_wrnh = var_wrnh.children[arg_rcsn]
            else:
                break
        return ''.join(var_ayzf)


class Solution:

    def func_wnki(arg_ihhe, arg_egyk, arg_dcmd):
        if not arg_dcmd:
            return ''
        if var_llti(arg_dcmd) == 1:
            return arg_dcmd[0]
        var_zbxo = var_rdmc()
        for var_rjut in arg_dcmd[1:]:
            var_zbxo.insert(var_rjut)
        return var_zbxo.searchLongestPrefix(arg_egyk)

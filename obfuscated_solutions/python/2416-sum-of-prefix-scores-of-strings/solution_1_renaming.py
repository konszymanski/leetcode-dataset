class trie_node:

    def func_udax(arg_ihhe):
        arg_ihhe.next = [None] * 26
        arg_ihhe.cnt = 0


class Solution:

    def func_udax(arg_ihhe):
        arg_ihhe.root = var_xdvx()

    def func_rcsn(arg_ihhe, arg_bacg):
        var_hqta = arg_ihhe.root
        for var_rgwu in arg_bacg:
            if var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')] is None:
                var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')] = var_xdvx()
            var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')].cnt += 1
            var_hqta = var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')]

    def func_osiz(arg_ihhe, arg_ayzf):
        var_hqta = arg_ihhe.root
        var_wnki = 0
        for var_rgwu in arg_ayzf:
            var_wnki += var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')].cnt
            var_hqta = var_hqta.next[var_wrnh(var_rgwu) - var_wrnh('a')]
        return var_wnki

    def func_egyk(arg_ihhe, arg_dcmd):
        var_llti = var_zbxo(arg_dcmd)
        for var_rdmc in var_rjut(var_llti):
            arg_ihhe.insert(arg_dcmd[var_rdmc])
        var_lsgw = [0] * var_llti
        for var_rdmc in var_rjut(var_llti):
            var_lsgw[var_rdmc] = arg_ihhe.count(arg_dcmd[var_rdmc])
        return var_lsgw

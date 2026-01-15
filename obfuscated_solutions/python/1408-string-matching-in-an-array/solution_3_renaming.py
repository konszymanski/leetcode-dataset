class Solution:


    class TrieNode:

        def func_udax(arg_ihhe):
            arg_ihhe.frequency = 0
            arg_ihhe.child_nodes = {}

    def func_xdvx(arg_ihhe, arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = []
        var_wrnh = arg_ihhe.TrieNode()
        for var_osiz in arg_rcsn:
            for var_ayzf in var_wnki(var_egyk(var_osiz)):
                arg_ihhe._insert_word(var_wrnh, var_osiz[var_ayzf:])
        for var_osiz in arg_rcsn:
            if arg_ihhe._is_substring(var_wrnh, var_osiz):
                var_rgwu.append(var_osiz)
        return var_rgwu

    def func_dcmd(arg_ihhe, var_wrnh: 'TrieNode', var_osiz: var_hqta) ->None:
        var_llti = var_wrnh
        for var_zbxo in var_osiz:
            if var_zbxo not in var_llti.child_nodes:
                var_llti.child_nodes[var_zbxo] = arg_ihhe.TrieNode()
            var_llti = var_llti.child_nodes[var_zbxo]
            var_llti.frequency += 1

    def func_rdmc(arg_ihhe, var_wrnh: 'TrieNode', var_osiz: var_hqta
        ) ->var_rjut:
        var_llti = var_wrnh
        for var_zbxo in var_osiz:
            var_llti = var_llti.child_nodes[var_zbxo]
        return var_llti.frequency > 1

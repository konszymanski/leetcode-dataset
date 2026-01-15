class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.children = {}
        arg_ihhe.is_word = False


class Solution:

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta, arg_bacg: var_rgwu[var_hqta]
        ) ->var_cbvh:
        var_wrnh = var_osiz(arg_rcsn)
        var_ayzf = arg_ihhe.buildTrie(arg_bacg)

        @var_lsgw
        def func_wnki(arg_egyk):
            if arg_egyk == var_wrnh:
                return 0
            var_dcmd = func_wnki(arg_egyk + 1) + 1
            var_llti = var_ayzf
            for var_zbxo in var_rdmc(arg_egyk, var_wrnh):
                if arg_rcsn[var_zbxo] not in var_llti.children:
                    break
                var_llti = var_llti.children[arg_rcsn[var_zbxo]]
                if var_llti.is_word:
                    var_dcmd = var_rjut(var_dcmd, func_wnki(var_zbxo + 1))
            return var_dcmd
        return func_wnki(0)

    def func_yjch(arg_ihhe, arg_bacg):
        var_ayzf = var_dmio()
        for var_ulfl in arg_bacg:
            var_llti = var_ayzf
            for var_lgvi in var_ulfl:
                if var_lgvi not in var_llti.children:
                    var_llti.children[var_lgvi] = var_dmio()
                var_llti = var_llti.children[var_lgvi]
            var_llti.is_word = True
        return var_ayzf

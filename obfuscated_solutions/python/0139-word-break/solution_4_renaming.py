class TrieNode:

    def func_udax(arg_ihhe):
        arg_ihhe.is_word = False
        arg_ihhe.children = {}


class Solution:

    def func_xdvx(arg_ihhe, arg_rcsn: var_hqta, arg_bacg: var_rgwu[var_hqta]
        ) ->var_lsgw:
        var_wrnh = var_osiz()
        for var_ayzf in arg_bacg:
            var_wnki = var_wrnh
            for var_egyk in var_ayzf:
                if var_egyk not in var_wnki.children:
                    var_wnki.children[var_egyk] = var_osiz()
                var_wnki = var_wnki.children[var_egyk]
            var_wnki.is_word = True
        var_dcmd = [False] * var_llti(arg_rcsn)
        for var_zbxo in var_rdmc(var_llti(arg_rcsn)):
            if var_zbxo == 0 or var_dcmd[var_zbxo - 1]:
                var_wnki = var_wrnh
                for var_rjut in var_rdmc(var_zbxo, var_llti(arg_rcsn)):
                    var_egyk = arg_rcsn[var_rjut]
                    if var_egyk not in var_wnki.children:
                        break
                    var_wnki = var_wnki.children[var_egyk]
                    if var_wnki.is_word:
                        var_dcmd[var_rjut] = True
        return var_dcmd[-1]

class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_osiz:
        var_rgwu = arg_ihhe._Trie()
        for var_wrnh in arg_xdvx:
            var_rgwu._add_word(var_wrnh)
        return var_rgwu._count_prefix(arg_rcsn)


    class _Trie:


        class _Node:

            def func_ayzf(arg_ihhe):
                arg_ihhe.links = [None] * 26
                arg_ihhe.count = 0

        def func_ayzf(arg_ihhe):
            arg_ihhe.root = arg_ihhe._Node()

        def func_wnki(arg_ihhe, var_wrnh: var_hqta) ->None:
            var_egyk = arg_ihhe.root
            for var_dcmd in var_wrnh:
                var_llti = var_zbxo(var_dcmd) - var_zbxo('a')
                if var_egyk.links[var_llti] is None:
                    var_egyk.links[var_llti] = arg_ihhe._Node()
                var_egyk = var_egyk.links[var_llti]
                var_egyk.count += 1

        def func_rdmc(arg_ihhe, arg_rcsn: var_hqta) ->var_osiz:
            var_egyk = arg_ihhe.root
            for var_dcmd in arg_rcsn:
                var_llti = var_zbxo(var_dcmd) - var_zbxo('a')
                if var_egyk.links[var_llti] is None:
                    return 0
                var_egyk = var_egyk.links[var_llti]
            return var_egyk.count

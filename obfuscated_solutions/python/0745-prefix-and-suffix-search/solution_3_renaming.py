var_udax = lambda : var_ihhe.defaultdict(var_udax)
var_xdvx = False


class WordFilter:

    def func_rcsn(arg_bacg, arg_hqta: var_rgwu[var_wrnh]):
        arg_bacg.trie = var_udax()
        for var_osiz, var_ayzf in var_wnki(arg_hqta):
            var_ayzf += '#'
            for var_egyk in var_dcmd(var_llti(var_ayzf)):
                var_zbxo = arg_bacg.trie
                var_zbxo[var_xdvx] = var_osiz
                for var_rdmc in var_dcmd(var_egyk, 2 * var_llti(var_ayzf) - 1):
                    var_zbxo = var_zbxo[var_ayzf[var_rdmc % var_llti(var_ayzf)]
                        ]
                    var_zbxo[var_xdvx] = var_osiz

    def func_rjut(arg_bacg, arg_lsgw: var_wrnh, arg_cbvh: var_wrnh) ->var_dmio:
        var_zbxo = arg_bacg.trie
        for var_yjch in (arg_cbvh + '#' + arg_lsgw):
            if var_yjch not in var_zbxo:
                return -1
            var_zbxo = var_zbxo[var_yjch]
        return var_zbxo[var_xdvx]

var_udax = lambda : var_ihhe.defaultdict(var_udax)
var_xdvx = False


class WordFilter:

    def func_rcsn(arg_bacg, arg_hqta: var_rgwu[var_wrnh]):
        arg_bacg.trie = var_udax()
        for var_osiz, var_ayzf in var_wnki(arg_hqta):
            var_egyk = arg_bacg.trie
            var_egyk[var_xdvx] = var_osiz
            for var_dcmd, var_llti in var_wnki(var_ayzf):
                var_zbxo = var_egyk
                for var_rdmc in var_ayzf[var_dcmd:]:
                    var_zbxo = var_zbxo[var_rdmc, None]
                    var_zbxo[var_xdvx] = var_osiz
                var_zbxo = var_egyk
                for var_rdmc in var_ayzf[:-var_dcmd or None][::-1]:
                    var_zbxo = var_zbxo[None, var_rdmc]
                    var_zbxo[var_xdvx] = var_osiz
                var_egyk = var_egyk[var_llti, var_ayzf[~var_dcmd]]
                var_egyk[var_xdvx] = var_osiz

    def func_rjut(arg_bacg, arg_lsgw: var_wrnh, arg_cbvh: var_wrnh) ->var_lgvi:
        var_egyk = arg_bacg.trie
        for var_yjch, var_dmio in var_ulfl(arg_lsgw, arg_cbvh[::-1]):
            if (var_yjch, var_dmio) not in var_egyk:
                return -1
            var_egyk = var_egyk[var_yjch, var_dmio]
        return var_egyk[var_xdvx]

class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_rgwu,
        arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_zbxo[var_zbxo[var_rgwu]]:
        var_wrnh = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        var_osiz = []
        var_ayzf = 1
        var_wnki = 0
        while var_egyk(var_osiz) < arg_xdvx * arg_rcsn:
            for var_dcmd in var_llti(2):
                for var_dcmd in var_llti(var_ayzf):
                    if (arg_bacg >= 0 and arg_bacg < arg_xdvx and arg_hqta >=
                        0 and arg_hqta < arg_rcsn):
                        var_osiz.append([arg_bacg, arg_hqta])
                    arg_bacg += var_wrnh[var_wnki][0]
                    arg_hqta += var_wrnh[var_wnki][1]
                var_wnki = (var_wnki + 1) % 4
            var_ayzf += 1
        return var_osiz
